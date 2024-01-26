from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, UsersViewSet, BookingsViewSet, MenuItemsViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='user')
router.register(r'bookings', BookingsViewSet, basename='booking')
router.register(r'menu-items', MenuItemsViewSet, basename='menu-item')

urlpatterns = [
  path('', include(router.urls)),
  # path('', index.as_view(), name='index'),
]