from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, TableBookingViewSet


router = DefaultRouter()
router.register(r'menu', MenuItemViewSet, basename='menu')
router.register(r'tablebooking', TableBookingViewSet, basename='tablebooking')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),  # Djoser authentication routes
    path('auth/', include('djoser.urls.jwt')),
]
