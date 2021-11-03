from rest_framework import status

from .base_file import BaseTestCase


class TestAuthenticationApi(BaseTestCase):
    """ Class test the menu"""

    def test_registration(self):
        """ Test creation of a menu """
   
        response = self.login_user()

        response = self.client.post(
            self.login_url,
            self.login_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['message'],
            "You have logged in successfully")

