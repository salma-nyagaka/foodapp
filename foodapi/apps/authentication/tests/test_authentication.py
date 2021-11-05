import json
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
    
    def test_unauthorized_user(self):
        """ Test unauthorized user """

        data = self.unauthorized_user()
        response = json.loads(data.content)
        self.assertEqual(data.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response['error'],
            "You are now allowed to view this resource")

    def test_registration_blank_credentials(self):
        """ Test registration of a new user with no data """

        response = self.create_user_no_data()
        res = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
        self.assertEqual(
            res['error'],
            {'email': ['Please fill in the email.'], 
            'username':['Please fill in the username.'], 
            'password': ['Please fill in the password.'], 
            'role': ['"" is not a valid choice.']})

    def test_login(self):
        """ Test user login """

        response = self.login_user()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['message'],
            "You have logged in successfully")

    def test_login_wrong_credentials(self):
        """ Test user login """

        response = self.create_user()

        login_res = self.client.post(
            self.login_url,
            self.login_wrong_data,
            format="json"
        )
        data = json.loads(login_res.content)
      
        self.assertEqual(login_res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            data['error'],
            {'non_field_errors': ['Either your email or password is not right. Kindly double check them ']})

    def test_get_user(self):
        """ Test get user by email"""
        user = self.get_user_email()
        self.assertEqual(user.email,
            "admin@gmail.com")

    def test_get_all_users(self):
        """ Test to get all users """
        response = self.get_all_users()

        self.assertEqual(
            response['message'],
            "All users have been fetched successfully")

    def test_get_one_user(self):
        """ Test to get a single user """
        response = self.get_one_user()

        self.assertEqual(
            response['message'],
            "User details have been fetched successfully")

    def test_delete_one_user(self):
        """ Test to delete a single user """
        response = self.delete_one_user()

        self.assertEqual(
            response['message'],
            "User has been deleted successfully")