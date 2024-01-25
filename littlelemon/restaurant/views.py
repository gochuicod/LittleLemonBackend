from django.views.generic.base import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Booking, MenuItem
from .serializers import UserSerializer, BookingSerializer, MenuItemSerializer

# Create your views here.
class index(TemplateView):
  template_name = 'index.html'

class MenuItemsViewSet(ModelViewSet):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]

class BookingsViewSet(ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]

class UsersViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]