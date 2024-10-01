from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        item_id = self.kwargs.get('pk')
        cached_item = cache.get(f'item_{item_id}')
        if cached_item:
            return cached_item
        item = super().get_object()
        cache.set(f'item_{item_id}', item)
        return item
    
    def perform_update(self, serializer):
        instance = serializer.save()
        
        cache_key = f'item_{instance.pk}'
        cache.delete(cache_key)

    def perform_destroy(self, instance):
        cache_key = f'item_{instance.pk}'
        cache.delete(cache_key)
        instance.delete()


    