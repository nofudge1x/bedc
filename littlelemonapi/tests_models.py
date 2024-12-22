# tests_models.py
from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(name="IceCream", price=80)
        self.assertEqual(str(item), "IceCream : 80") 
