from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Booking, MenuItem
import bleach

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['url','username','email','groups']

class BookingSerializer(ModelSerializer):
  class Meta:
    model = Booking
    fields = ['id','name','no_of_guests','booking_date']

  def validate(self, attrs):
    attrs['name'] = bleach.clean(attrs['name'])
    return super().validate(attrs)

class MenuSerializer(ModelSerializer):
  class Meta:
    model = MenuItem
    fields = ['id','title','price','inventory']

  def validate(self, attrs):
    attrs['title'] = bleach.clean(attrs['title'])
    return super().validate(attrs)