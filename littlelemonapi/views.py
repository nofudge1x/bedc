from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import MenuItem, TableBooking
from .serializers import MenuItemSerializer, TableBookingSerializer

# MenuItem ViewSet
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    

# TableBooking ViewSet
class TableBookingViewSet(viewsets.ModelViewSet):
    
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
