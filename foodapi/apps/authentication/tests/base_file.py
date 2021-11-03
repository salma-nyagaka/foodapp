from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase


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
        self.login_data = {
            "email": "admin@gmail.com",
            "username": "admin",
            "password": "admin123",
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
