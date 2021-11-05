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
        self.all_users_url = reverse("all_users")

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
        """ Function to create a user"""
        response = self.client.post(
            self.registration_url,
            self.registration_data,
            **{'QUERY_STRING': 'is_admin=is_admin'},
            format="json"
        )

        return response

    def unauthorized_user(self):
        """ Function to send a req
        without params"""
        response = self.client.post(
            self.registration_url,
            self.registration_data,
            format="json"
        )

        return response

    def invalid_params(self):
        """ Function to send a request
        with invalid params"""
        response = self.client.post(
            self.registration_url,
            self.registration_data,
            **{'QUERY_STRING': 'kkk=kkk'},
            format="json"
        )

        return response

    def create_user_no_data(self):
        """ Create a user to be used by some test cases"""
        response = self.client.post(
            self.registration_url,
            self.registration_data_no_data,
            **{'QUERY_STRING': 'is_admin=is_admin'},
            format="json"
        )

        return response

    def get_user_email(self):
        """ Get user by email """
        response = self.create_user()

        data = json.loads(response.content)
        user = User.objects.get(email=data['data']['email'])

        return user

    def login_user(self):
        """ Test to log in a user"""
        response = self.create_user()

        response = self.client.post(
            self.login_url,
            self.login_data,
            format="json"
        )

        return response

    def get_all_users(self):
        """ Function to delete a user """

        response = self.login_user()

        data = json.loads(response.content)
        response = self.client.get(
            self.all_users_url,
            HTTP_AUTHORIZATION="Bearer {}".format(data['data']['token']),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def get_one_user(self):
        """ Function to get a user """

        login_res = self.login_user()
        token = json.loads(login_res.content)
        data = User.objects.all().first()

        self.single_user_url = reverse(
            "single_user", kwargs={"user_id": data.id})

        response = self.client.get(
            self.single_user_url,
            HTTP_AUTHORIZATION="Bearer {}".format(token['data']['token']),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def get_nonexistant_user(self):
        """ Function to get a who does not exist """

        login_res = self.login_user()
        token = json.loads(login_res.content)

        self.single_user_url = reverse("single_user", kwargs={"user_id": 100})

        response = self.client.get(
            self.single_user_url,
            HTTP_AUTHORIZATION="Bearer {}".format(token['data']['token']),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def delete_one_user(self):
        """ Function to delete a user """

        login_res = self.login_user()
        token = json.loads(login_res.content)
        data = User.objects.all().first()

        self.single_user_url = reverse(
            "single_user", kwargs={"user_id": data.id})

        response = self.client.delete(
            self.single_user_url,
            HTTP_AUTHORIZATION="Bearer {}".format(token['data']['token']),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res
