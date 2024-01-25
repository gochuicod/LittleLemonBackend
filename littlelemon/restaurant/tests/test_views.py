from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from ..models import MenuItem, Booking

class MenuItemsViewSetTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpassword')
    self.client = APIClient()
    self.client.force_authenticate(user=self.user)
    self.menu_item_data = {
      'title': 'Pancake',
      'price': 200,
      'inventory': 10,
    }
    self.menu_item = MenuItem.objects.create(**self.menu_item_data)

  def test_list_menu_items(self):
    response = self.client.get('/api/menu-items/')
    self.assertEqual(response.status_code, HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_get_menu_item(self):
    response = self.client.get('/api/menu-items/1/')
    self.assertEqual(response.status_code, HTTP_200_OK)
    self.assertEqual(len(response.data), 4)

  def test_create_menu_item(self):
    new_menu_item_data = {
      'title': 'Hotdog',
      'price': 50,
      'inventory': 500
    }

    response = self.client.post('/api/menu-items/', new_menu_item_data,format='json')
    self.assertEqual(response.status_code, HTTP_201_CREATED)

    created_menu_item = response.data
    self.assertEqual(created_menu_item['title'], new_menu_item_data['title'])

    updated_response = self.client.get('/api/menu-items/')
    self.assertEqual(len(updated_response.data), 2)

  def test_update_menu_item(self):
    updated_menu_item_data = {
      'title': 'Pancake',
      'price': '40.00',
      'inventory': 100,
    }

    response = self.client.put('/api/menu-items/1/', updated_menu_item_data, format='json')
    self.assertEqual(response.status_code, HTTP_200_OK)

    updated_menu_item = response.data
    self.assertEqual(updated_menu_item['title'], updated_menu_item_data['title'])
    self.assertEqual(updated_menu_item['price'], updated_menu_item_data['price'])
    self.assertEqual(updated_menu_item['inventory'], updated_menu_item_data['inventory'])

    updated_response = self.client.get('/api/menu-items/1/')
    self.assertEqual(updated_response.data['title'], updated_menu_item['title'])
    self.assertEqual(updated_response.data['price'], updated_menu_item['price'])
    self.assertEqual(updated_response.data['inventory'], updated_menu_item['inventory'])

  def test_patch_menu_item(self):
    partial_update_data = {
      'title': 'Pancake',
      'price': '35.00'
    }

    response = self.client.patch('/api/menu-items/1/', partial_update_data, format='json')
    self.assertEqual(response.status_code, HTTP_200_OK)

    updated_menu_item = response.data
    self.assertEqual(updated_menu_item['price'], partial_update_data['price'])

    updated_response = self.client.get('/api/menu-items/1/')
    self.assertEqual(updated_response.data['price'], updated_menu_item['price'])

  def test_delete_menu_item(self):
    response = self.client.delete('/api/menu-items/1/')
    self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    updated_response = self.client.get('/api/menu-items/')
    self.assertEqual(len(updated_response.data), 0)

class BookingsViewSetTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpassword')
    self.client = APIClient()
    self.client.force_authenticate(user=self.user)
    self.booking_data = {
      'name': 'John Doe',
      'no_of_guests': 5,
      'booking_date': '2024-01-25T14:01:37.173973Z'
    }
    self.booking = Booking.objects.create(**self.booking_data)

  def test_list_bookings(self):
    response = self.client.get('/api/booking/tables/')
    self.assertEqual(response.status_code, HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

  def test_get_booking(self):
    response = self.client.get('/api/booking/tables/1/')
    self.assertEqual(response.status_code, HTTP_200_OK)
    self.assertEqual(len(response.data), 4)

  def test_create_booking(self):
    new_booking_data = {
      'name': 'Jane Doe',
      'no_of_guests': 4,
      'booking_date': '2024-01-25T14:01:37.173973Z',
    }

    response = self.client.post('/api/booking/tables/', new_booking_data, format='json')
    self.assertEqual(response.status_code, HTTP_201_CREATED)

    created_booking = response.data
    self.assertEqual(created_booking['name'], new_booking_data['name'])

    updated_response = self.client.get('/api/booking/tables/')
    self.assertEqual(len(updated_response.data), 2)

  def test_update_booking(self):
    updated_booking_data = {
      'name': 'Jane Doe',
      'no_of_guests': 3,
      'booking_date': '2024-01-25T14:01:37.173973Z',
    }

    response = self.client.put('/api/booking/tables/1/', updated_booking_data, format='json')
    self.assertEqual(response.status_code, HTTP_200_OK)

    updated_booking = response.data
    self.assertEqual(updated_booking['name'], updated_booking_data['name'])
    self.assertEqual(updated_booking['no_of_guests'], updated_booking_data['no_of_guests'])
    self.assertEqual(updated_booking['booking_date'], updated_booking_data['booking_date'])

    updated_response = self.client.get('/api/booking/tables/1/')
    self.assertEqual(updated_response.data['name'], updated_booking['name'])
    self.assertEqual(updated_response.data['no_of_guests'], updated_booking['no_of_guests'])
    self.assertEqual(updated_response.data['booking_date'], updated_booking['booking_date'])

  def test_patch_menu_item(self):
    partial_update_data = {
      'name': 'Jane Doe',
      'no_of_guests': 2
    }

    response = self.client.patch('/api/booking/tables/1/', partial_update_data, format='json')
    self.assertEqual(response.status_code, HTTP_200_OK)

    updated_booking = response.data
    self.assertEqual(updated_booking['no_of_guests'], partial_update_data['no_of_guests'])

    updated_response = self.client.get('/api/booking/tables/1/')
    self.assertEqual(updated_response.data['no_of_guests'], updated_booking['no_of_guests'])

  def test_delete_booking(self):
    response = self.client.delete('/api/booking/tables/1/')
    self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    updated_response = self.client.get('/api/booking/tables/')
    self.assertEqual(len(updated_response.data), 0)