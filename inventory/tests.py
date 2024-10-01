from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):

    def setUp(self):
        # Set up a user and obtain a JWT token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'testpassword'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.item = Item.objects.create(name='Item2',asset_id='human2113', description='Another item')

    def test_create_item(self):
        url = reverse('create_item')
        data = {'name': 'Item1', 'asset_id':'human23','description': 'A sample item'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_item(self):
        
        url = reverse('retrieve_update_delete_item', kwargs={'pk': self.item.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        url = reverse('retrieve_update_delete_item', args=[self.item.id])
        data = {'name': 'Updated Item', 'asset_id':'as123','description': 'Updated Description'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the item was updated in the database
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.description, 'Updated Description')

    def test_delete_item(self):
        url = reverse('retrieve_update_delete_item', args=[self.item.id])
        response = self.client.delete(url)

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the item was deleted from the database
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=self.item.id)
