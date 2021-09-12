from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from django.urls import reverse

from account.models import User, UserType
from restaurant.models import Restaurant


class TestRestaurant(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.register_url = reverse('register')

        self.emp_user_data = {'username': "employee", 'user_types': UserType.EMPLOYEE, "password": "password1@212"}
        self.owner_user_data = {'username': "owner", 'user_types': UserType.OWNER, "password": "password1@212"}
        return super().setUp()

    def register_employee(self):
        return User.objects.create_user(**self.emp_user_data)

    def register_owner(self):
        return User.objects.create_user(**self.owner_user_data)

    def test_create_restaurant(self):
        owner = self.register_owner()
        self.assertEqual(owner.user_types, "OWNER")
        restaurant = Restaurant.objects.create(name='some name', owner=owner)
        self.assertEqual(restaurant.name, "some name")
        self.assertEqual(str(restaurant), "some name")
        self.assertFalse(restaurant.owner.user_types == "ADMIN")

    def test_except_owner_user_cant_create_restaurant(self):
        employee = self.register_employee()
        self.assertRaises(ValidationError, Restaurant.objects.create, name='some name', owner=employee)





