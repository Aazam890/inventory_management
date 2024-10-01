from django.urls import path
from .views import ItemCreateView, ItemRetrieveUpdateDeleteView

urlpatterns = [
    path('items/', ItemCreateView.as_view(), name='create_item'),
    path('items/<int:pk>/', ItemRetrieveUpdateDeleteView.as_view(), name='retrieve_update_delete_item'),
]
