from rest_framework import status

from .base_file import BaseTestCase
from django.conf import settings


class TestAuthenticationApi(BaseTestCase):
    """ Class test the auth API"""

    def test_registration(self):
        """ Test registration of a new user """

        response = self.create_user()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data['message'],
            "Your account has been created successfully")

    def test_login(self):
        """ Test user login """

        response = self.create_user()

        response = self.client.post(
            self.login_url,
            self.login_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['message'],
            "You have logged in successfully")

    def expired_token(self):
        """ Test login with expired token """
