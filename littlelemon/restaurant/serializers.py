from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Booking, MenuItem
import bleach

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['url','username','email','groups']

  def validate(self, data):
    data['username'] = bleach.clean(data['username'])
    data['email'] = bleach.clean(data['email'])
    return data

class BookingSerializer(ModelSerializer):
  class Meta:
    model = Booking
    fields = ['id','name','no_of_guests','booking_date']

  def validate(self, data):
    data['name'] = bleach.clean(data['name'])
    return data

class MenuItemSerializer(ModelSerializer):
  class Meta:
    model = MenuItem
    fields = ['id','title','price','inventory']

  def validate(self, data):
    data['title'] = bleach.clean(data['title'])
    return data