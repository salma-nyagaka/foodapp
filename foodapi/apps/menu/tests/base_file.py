import json
from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase

from foodapi.apps.menu.models import Menu


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the package"""

    def setUp(self):

        self.client = APIClient()
        # Access urls for testing
        self.create_menu_url = reverse("menu")
        self.all_menu_url = reverse("all_menu")
        self.login_url = reverse("user_login")

        self.registration_url = reverse("user_registration")
        self.login_url = reverse("user_login")

        # Create dummy data for testing
        self.create_menu_data = {
            "name": "Burger",
            "price": 300,
            "description": "Lettuce with bacon and Cheese inside grilled buns"
        }
        self.create_menu_data_no_data = {
            "name": "",
            "description": ""
        }

        self.update_menu_data = {
            "name": "Cheese Burger"
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

        self.attendant_registration_data = {
            "email": "attendant@gmail.com",
            "username": "attendant",
            "password": "attendant123",
            "role": "FOOD_ATTENDANT"

        }

        self.attendant_login_data = {
            "email": "attendant@gmail.com",
            "username": "attendant",
            "password": "attendant123",
            "role": "FOOD_ATTENDANT"
        }

    def create_user(self):
        """ Create a user to be used by some test cases"""
        admin_response = self.client.post(
            self.registration_url,
            self.registration_data,
            **{'QUERY_STRING': 'is_admin=is_admin'},
            format="json"
        )
        attendant_response = self.client.post(
            self.registration_url,
            self.attendant_registration_data,
            **{'QUERY_STRING':'is_admin=is_admin'},
            format="json"
        )
        return admin_response, attendant_response

    def login_user(self):
        """ Login User """

        admin_login_data, attendant_login_data, = self.create_user()

        admin_json_data = json.loads(admin_login_data.content)
        admin_user_data = admin_json_data['data']
        admin_user_data['password'] = 'admin123'


        attedant_json_data = json.loads(attendant_login_data.content)
        attedant_user_data = attedant_json_data['data']
        attedant_user_data['password'] = 'attendant123'

   
        admin_response = self.client.post(
            self.login_url,
            admin_json_data['data'],
            format="json"
                )
        attendant_response = self.client.post(
            self.login_url,
            attedant_json_data['data'],
            format="json"

                )
       
        admin_res_data = json.loads(admin_response.content)
        attendant_res_data = json.loads(attendant_response.content)
      

        admin_token = admin_res_data['data']['token']
        attendant_token = attendant_res_data['data']['token']

        return admin_token, attendant_token


    def create_menu(self):
        """ Function to create menu"""
        token = self.login_user()

        response = self.client.post(
            self.create_menu_url,
            self.create_menu_data,
            HTTP_AUTHORIZATION="Bearer {}".format(token[0]),
            format="json"
        )
        menu_res = json.loads(response.content)

        return menu_res, token

    # def create_menu_forbidden(self):
    #     """ Function to create menu by 
    #     forbidden user"""
    #     token = self.create_menu()
    #     response = self.client.post(
    #         self.create_menu_url,
    #         self.create_menu_data,
    #         HTTP_AUTHORIZATION="Bearer {}".format(token[1][0]),
    #         format="json"
    #     )
    
    #     menu_res = json.loads(response.content)

    #     return menu_res, token

    def create_menu_no_data(self):
        """ Function to create menu"""
        token = self.login_user()

        response = self.client.post(
            self.create_menu_url,
            self.create_menu_data_no_data,
            HTTP_AUTHORIZATION="Bearer {}".format(token[0]),
            format="json"
        )
        menu_res = json.loads(response.content)

        return menu_res

    def get_all_menus(self):
        """ Function to get all menu items"""
        menu = self.create_menu()

        response = self.client.get(
            self.all_menu_url,
            HTTP_AUTHORIZATION="Bearer {}".format(menu[1][0]),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def get_single_menu(self):
        """ Function to get a single menu item """
        menu = self.create_menu()

        data = Menu.objects.all().first()
        self.single_menu_url = reverse(
            "single_menu_item", kwargs={'menu_id': data.id})
        response = self.client.get(
            self.single_menu_url,
            HTTP_AUTHORIZATION="Bearer {}".format(menu[1][0]),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def get_menu_does_not_exist(self):
        """ Function to get a single menu item 
        that does not exist """
        menu = self.create_menu()

        self.single_menu_url = reverse(
            "single_menu_item", kwargs={'menu_id': "1"})
        response = self.client.get(
            self.single_menu_url,
            HTTP_AUTHORIZATION="Bearer {}".format(menu[1][0]),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def update_single_menu(self):
        """ Function to update a single menu item """
        menu = self.create_menu()

        data = Menu.objects.all().first()
        self.single_menu_url = reverse(
            "single_menu_item", kwargs={'menu_id': data.id})
        response = self.client.put(
            self.single_menu_url,
            self.update_menu_data,
            HTTP_AUTHORIZATION="Bearer {}".format(menu[1][0]),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def delete_single_menu(self):
        """ Function to delete a single menu item """
        menu = self.create_menu()
    
        data = Menu.objects.all().first()
        self.single_menu_url = reverse(
            "single_menu_item", kwargs={'menu_id': data.id})
        response = self.client.delete(
            self.single_menu_url,
            HTTP_AUTHORIZATION="Bearer {}".format(menu[1][0]),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    def delete_single_menu_invalid_token(self):
        """ Function to delete a single menu item with invalid token """
        menu = self.create_menu()

        data = Menu.objects.all().first()
        self.single_menu_url = reverse(
            "single_menu_item", kwargs={'menu_id': data.id})
        response = self.client.delete(
            self.single_menu_url,
            HTTP_AUTHORIZATION="Bearer {}".format('123'),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res
