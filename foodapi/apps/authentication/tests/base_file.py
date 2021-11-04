import json
from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase

from foodapi.apps.authentication.models import User
class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the package"""

    def setUp(self):

        self.client = APIClient()
        # Access urls for testing
        self.registration_url = reverse("user_registration")
        self.login_url = reverse("user_login")

        # Create dummy data for testing
        self.registration_data = {
            "email": "admin@gmail.com",
            "username": "admin",
            "password": "admin123",
            "role": "ADMIN"

        }

        self.registration_data_no_data = {
            "email": "",
            "username": "",
            "password": "",
            "role": ""

        }

        self.login_data = {
            "email": "admin@gmail.com",
            "username": "admin",
            "password": "admin123",
            "role": "ADMIN"
        }

        self.login_wrong_data = {
                "email": "admin@gmail.com",
                "username": "admin",
                "password": "admin123678",
                "role": "ADMIN"
            }

    def create_user(self):
        """ Create a user to be used by some test cases"""
        response = self.client.post(
            self.registration_url,
            self.registration_data,
            **{'QUERY_STRING':'is_admin=is_admin'},
            format="json"
        )

        return response

    def create_user_no_data(self):
        """ Create a user to be used by some test cases"""
        response = self.client.post(
            self.registration_url,
            self.registration_data_no_data,
            **{'QUERY_STRING':'is_admin=is_admin'},
            format="json"
        )

        return response

    def get_user_email(self):
        """ Get user by email """
        response = self.create_user()
       
        data = json.loads(response.content)
        user = User.objects.get(email=data['data']['email'])

        return user

