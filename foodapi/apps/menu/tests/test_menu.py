from rest_framework import status

from .base_file import BaseTestCase


class TestAuthenticationApi(BaseTestCase):
    """ Class test the menu"""

    def test_create_menu(self):
        """ Test creation of a menu """
   
        response = self.create_menu()
        self.assertEqual(
            response[0]['message'],
            "Menu has been created successfully")

    
    def test_create_menu_n_data(self):
        """ Test creation of a menu with no data"""
   
        response = self.create_menu_no_data()
        # import pdb
        # pdb.set_trace()
        self.assertEqual(
            response['error'],
           {'name': ['This field may not be blank.'], 'description': ['This field may not be blank.']})

    def test_menu(self):
        """ Test get all menu items """

        response = self.get_all_menus()
        self.assertEqual(
            response['message'],
            "All menu items have been fetched successfully")

    

    def test_get_single_menu(self):
        """ Test get single menu item """

        response = self.get_single_menu()
     
        self.assertEqual(
            response['message'],
            "Menu item has been fetched successfully")

    def test_update_single_menu(self):
        """ Test to update a menu item """
        response = self.update_single_menu()
        self.assertEqual(
            response['message'],
            "The menu item has been updated successfully")


    def test_delete_single_menu(self):
        """ Test to delete a menu item """
        response = self.delete_single_menu()
        self.assertEqual(
            response['message'],
            "Menu item has been deleted successfully")


    def test_delete_single_menu_invalid_token(self):
        """ Test to delete a menu item  with invalid token """
        response = self.delete_single_menu_invalid_token()
        self.assertEqual(
            response,
            {'detail': 'Invalid token'})