from rest_framework import status

from .base_file import BaseTestCase
from foodapi.apps.menu.models import Menu

class TestMenuApi(BaseTestCase):
    """ Class test the menu"""

    def test_create_menu(self):
        """ Test creation of a menu """
   
        response = self.create_menu()
        self.assertEqual(
            response[0]['message'],
            "Menu has been created successfully")

    
    def test_create_menu_no_data(self):
        """ Test creation of a menu with no data"""
   
        response = self.create_menu_no_data()
        self.assertEqual(
            response['error'],
           {'name': ['This field may not be blank.'], 'description': ['This field may not be blank.']})

    # def test_get_all_menu_forbidden(self):
    #     """ Test create menu by forbidden user """

    #     res= self.create_menu_forbidden()
    #     self.assertEqual(
    #         res[0]['error'],
    #         "You are not allowed to perform this action") 
    
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


    def test_get_nonexistant_single_menu(self):
        """ Test get nonexistant single menu item """

        response = self.get_menu_does_not_exist()
     
        self.assertEqual(
            response['message'],
            "Menu item does not exist")

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
