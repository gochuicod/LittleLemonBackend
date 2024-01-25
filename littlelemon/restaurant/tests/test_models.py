from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from ..models import MenuItem, Booking

# Create your tests here.
class MenuItemTest(TestCase):
  def setUp(self):
    self.menu_item = {
      'title': 'Ice Cream',
      'price': 80,
      'inventory': 100
    }

  def test_get_menu_item(self):
    menu_item = MenuItem.objects.create(**self.menu_item)
    self.assertEqual(str(menu_item), "Ice Cream : 80")

  def test_create_menu_item(self):
    menu_item = MenuItem.objects.create(**self.menu_item)
    self.assertEqual(menu_item.title, 'Ice Cream')
    self.assertEqual(menu_item.price, 80)
    self.assertIsNotNone(menu_item.inventory)

  def test_menu_item_title_max_length(self):
    self.menu_item['title'] = 'A' * 256
    menu_item = MenuItem(**self.menu_item)
    with self.assertRaises(ValidationError):
      menu_item.clean_fields()

  def test_menu_item_price_max_value(self):
    self.menu_item['price'] = '99999999999.99'
    menu_item = MenuItem(**self.menu_item)
    with self.assertRaises(ValidationError):
      menu_item.clean_fields()

class BookingTest(TestCase):
  def setUp(self):
    self.booking = {
      'name': 'John Doe',
      'no_of_guests': 5,
      'booking_date': '2024-01-25 14:01:37.173973+00:00'
      # 'booking_date': timezone.now()
    }

  def test_get_booking(self):
    booking = Booking.objects.create(**self.booking)
    self.assertEqual(str(booking), "John Doe | Guests: 5 | Date: 2024-01-25 14:01:37.173973+00:00")

  def test_create_booking(self):
    booking = Booking.objects.create(**self.booking)
    self.assertEqual(booking.name, 'John Doe')
    self.assertEqual(booking.no_of_guests, 5)
    self.assertIsNotNone(booking.booking_date)

  def test_booking_name_max_length(self):
    self.booking['name'] = 'A' * 256
    booking = Booking(**self.booking)
    with self.assertRaises(ValidationError):
      booking.clean_fields()

  def test_no_of_guests_max_value(self):
    self.booking['no_of_guests'] = 1000000
    booking = Booking(**self.booking)
    with self.assertRaises(ValidationError):
      booking.clean_fields()