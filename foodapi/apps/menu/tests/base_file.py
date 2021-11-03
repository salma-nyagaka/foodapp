import json
from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the package"""

    def setUp(self):

        self.client = APIClient()
    #     # Access urls for testing
        self.create_menu_url = reverse("menu")
        self.login_url = reverse("user_login")

        self.registration_url = reverse("user_registration")
        self.login_url = reverse("user_login")

        # Create dummy data for testing
        self.create_menu_data = {
            "name": "Burger",
            "price": 300,
            "description": "Lettuce with bacon and Cheese inside grilled buns"
        }

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

    def login_user(self):
        """ Login User """
        login_data = self.create_user()
     
        json_data = json.loads(login_data.content)
        user_data = json_data['data']
        user_data['password'] = 'admin123'
        import pdb
        pdb.set_trace
        response = self.client.post(
            self.login_url,
            json_data['data'],
            format="json"
                )
        res_data = json.loads(response)
        token = res_data['data']['token']
        menu_res = self.client.post(
            self.create_menu_url,
            self.create_menu_data,
            HTTP_AUTHORIZATION="Bearer {}".format("token"),

            format="json"
        )
        import pdb
        pdb.set_trace()
        return menu_res

    # def create_menu(self):
    #     """ Create a menu to be used by some test cases"""
    #     import pdb
    #     pdb.set_trace()
    #     # user = self.login_user()

    def llogin_user(self):
        """ Login User """
        login_data = self.create_user()
     
        json_data = json.loads(login_data.content)
        user_data = json_data['data']
        user_data['password'] = 'admin123'
        import pdb
        pdb.set_trace
        response = self.client.post(
            self.login_url,
            json_data['data'],
            format="json"
                )
        res_data = json.loads(response)
        token = res_data['data']['token']
        return token

        # return response
