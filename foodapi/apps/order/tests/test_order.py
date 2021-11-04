from rest_framework import status

from .base_file import BaseTestCase


class TestOrderApi(BaseTestCase):
    """ Class to test the order"""

    def test_create_order(self):
        """ Test creation of an order """
   
        response = self.create_order()
        self.assertEqual(
            response[0]['message'],
            "Your order has been created successfully")

    def test_get_all_orders(self):
        """ Test get all orders """

        res= self.get_all_orders()
        self.assertEqual(
            res['message'],
            "All pending orders have been fetched successfully")
    
    # def test_get_all_orders_forbidden(self):
    #     """ Test get all orders by forbidden user """

    #     res= self.get_all_orders_forbidden()
    #     self.assertEqual(
    #         res['error'],
    #         "You are not allowed to perform this action") 
            
    def test_a_users_orders(self):
        """ Test get a user's orders """

        res_all, res_pending = self.get_users_orders()
        self.assertEqual(
            res_all['message'],
            "Your orders have been fetched successfully")
        self.assertEqual(
            res_pending['message'],
            "Your orders have been fetched successfully")


    def test_a_users_orders_no_params(self):
        """ Test get a user's orders with no 
        params provided"""

        res_all, res_pending = self.get_users_orders_no_params()
        self.assertEqual(
            res_all['error'],
            "Kindly pass 'all_orders' or 'pending_orders' in params")
        self.assertEqual(
            res_pending['error'],
            "Kindly pass 'all_orders' or 'pending_orders' in params")