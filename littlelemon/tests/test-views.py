from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Menu1", price = 10.99, description="Description1")

    def test_getall(self):
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)