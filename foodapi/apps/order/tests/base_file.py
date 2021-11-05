import json
from django.http import response
from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase
from foodapi.apps.menu.models import Menu
from foodapi.apps.authentication.models import User
from foodapi.apps.order.helpers.get_order_object import get_order_object


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the package"""

    def setUp(self):

        self.client = APIClient()

        # Access urls for testing
        self.registration_url = reverse("user_registration")
        self.login_url = reverse("user_login")
        self.create_order_url = reverse("order")
        self.create_menu_url = reverse("menu")
        self.all_orders_url = reverse("all_orders")
        self.user_order_url = reverse("user_orders")

        # Create dummy data for testing
        self.admin_registration_data = {
            "email": "admin@gmail.com",
            "username": "admin",
            "password": "admin123",
            "role": "ADMIN"

        }

        self.admin_login_data = {
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

        self.normal_user_registration_data = {
            "email": "normal@gmail.com",
            "username": "normal",
            "password": "normal123",
            "role": "NORMAL_USER"

        }

        self.normal_user_login_data = {
            "email": "normal@gmail.com",
            "username": "normal",
            "password": "normal123",
            "role": "NORMAL_USER"

        }

        self.create_menu_data = {
            "name": "Burger",
            "price": 300,
            "description": "Lettuce with bacon and Cheese inside grilled buns"
        }

    def create_user(self):
        """ Create a user to be used by some test cases"""
        admin_response = self.client.post(
            self.registration_url,
            self.admin_registration_data,
            **{'QUERY_STRING': 'is_admin=is_admin'},
            format="json"
        )

        attendant_response = self.client.post(
            self.registration_url,
            self.attendant_registration_data,
            **{'QUERY_STRING': 'is_admin=is_admin'},
            format="json"
        )

        normal_user_response = self.client.post(
            self.registration_url,
            self.normal_user_registration_data,
            **{'QUERY_STRING': 'is_admin=is_admin'},
            format="json"
        )

        return admin_response, attendant_response, normal_user_response

    def login_user(self):
        """ Login User """

        admin_login_data, aattendant_login_data, normal_user__login_data = self.create_user()

        admin_json_data = json.loads(admin_login_data.content)
        admin_user_data = admin_json_data['data']
        admin_user_data['password'] = 'admin123'

        attedant_json_data = json.loads(aattendant_login_data.content)
        attedant_user_data = attedant_json_data['data']
        attedant_user_data['password'] = 'attendant123'

        normal_json_data = json.loads(normal_user__login_data.content)
        normal_user_data = normal_json_data['data']
        normal_user_data['password'] = 'normal123'

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

        normal_user_response = self.client.post(
            self.login_url,
            normal_json_data['data'],
            format="json"
        )

        admin_res_data = json.loads(admin_response.content)
        attendant_res_data = json.loads(attendant_response.content)
        normal_res_data = json.loads(normal_user_response.content)

        admin_token = admin_res_data['data']['token']
        attendant_token = attendant_res_data['data']['token']
        normal_token = normal_res_data['data']['token']

        return admin_token, attendant_token, normal_token

    def create_menu(self):
        """ Function to create menu"""
        user_res = self.login_user()

        response = self.client.post(
            self.create_menu_url,
            self.create_menu_data,
            HTTP_AUTHORIZATION="Bearer {}".format(user_res[0]),
            format="json"
        )
        menu_res = json.loads(response.content)

        return menu_res, user_res

    def create_order(self):
        """ Function to create an order """
        menu_response = self.create_menu()
        menu_obj = Menu.objects.all().first()
        user_obj = User.objects.all().last()

        order_data = {
            "order": menu_obj.id,
            "user": user_obj.id
        }
        token = menu_response[1][0]

        response = self.client.post(
            self.create_order_url,
            order_data,
            HTTP_AUTHORIZATION="Bearer {}".format(token),
            format="json"
        )
        menu_res = json.loads(response.content)

        return menu_res, token, menu_response

    def get_all_orders(self):
        """ Function to get all orders made"""
        order = self.create_order()
        response = self.client.get(
            self.all_orders_url,
            HTTP_AUTHORIZATION="Bearer {}".format(order[2][1][1]),
            format="json"
        )
        menu_res = json.loads(response.content)
        return menu_res

    # def get_all_orders_forbidden(self):
    #     """ Function to get all orders from
    #     forbidden user """
    #     order = self.create_order()

    #     response = self.client.get(
    #         self.all_orders_url,
    #         HTTP_AUTHORIZATION="Bearer {}".format(order[2][1][2]),
    #         format="json"
    #             )
    #     menu_res = json.loads(response.content)
    #     return menu_res

    def get_users_orders(self):
        """ Function to get a user's orders """
        order = self.create_order()

        response_all = self.client.get(
            self.user_order_url,
            **{'QUERY_STRING': 'all_orders=all_orders'},
            HTTP_AUTHORIZATION="Bearer {}".format(order[2][1][1]),
            format="json"
        )
        response_pending = self.client.get(
            self.user_order_url,
            **{'QUERY_STRING': 'pending_orders=pending_orders'},
            HTTP_AUTHORIZATION="Bearer {}".format(order[2][1][1]),
            format="json"
        )
        res_all = json.loads(response_all.content)
        res_pending = json.loads(response_pending.content)
        return res_all, res_pending

    def get_users_orders_no_params(self):
        """ Function to get a user's orders
        with no params passed """
        order = self.create_order()

        response_all = self.client.get(
            self.user_order_url,
            HTTP_AUTHORIZATION="Bearer {}".format(order[2][1][1]),
            format="json"
        )
        response_pending = self.client.get(
            self.user_order_url,
            HTTP_AUTHORIZATION="Bearer {}".format(order[2][1][1]),
            format="json"
        )
        res_all = json.loads(response_all.content)
        res_pending = json.loads(response_pending.content)
        return res_all, res_pending
