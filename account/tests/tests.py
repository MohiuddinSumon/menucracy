from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from account.models import User


class TestRegisterView(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.register_url = reverse('register')

        self.emp_user_data = {'username': "employee", 'email': "email@test.com", "password": "password1@212"}
        self.owner_user_data = {'username': "owner", 'email': "email@test.com", "password": "password1@212"}
        return super().setUp()

    def register_employee(self):
        return User.objects.create_user(**self.emp_user_data)

    def register_owner(self):
        return User.objects.create_user(**self.owner_user_data)

    def test_create_user(self):
        employee_user = {'username': 'username', 'password': 'password1@212'}
        response = self.client.post(reverse('register'), employee_user)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creates_user(self):
        user = User.objects.create_user(username="username", email="email@test.com", password="password1@212")
        self.assertEqual(user.username, "username")
        self.assertFalse(user.is_staff)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(username="username", email="email@test.com", password="password1@212")
        self.assertEqual(user.username, "username")
        self.assertEqual(user.is_staff, True)

    def test_creates_super_user_with_is_staff(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username="username", email="email@test.com",
                          password="password1@212", is_staff=False)

        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                User.objects.create_superuser(is_staff=False, username="username", email="email@test.com",
                                              password="password1@212"))

    def test_creates_super_user_with_super_user_status(self):
        self.assertRaises(ValueError, User.objects.create_superuser, is_superuser=False, username="username",
                          email="email@test.com", password="password1@212")
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                User.objects.create_superuser(is_superuser=False, username="username", email="email@test.com",
                                              password="password1@212"))

    def test_cant_create_user_without_username(self):
        self.assertRaises(ValueError, User.objects.create_user, email=self.emp_user_data['email'],
                          password=self.emp_user_data['password'], username="")




