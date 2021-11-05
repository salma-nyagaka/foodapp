from rest_framework import status

from .base_file import BaseTestCase
from foodapi.apps.order.serializers import OrderSerializer


class TestOrderApi(BaseTestCase):
    """ Class to test the order serializers"""

    def test_size_lower_bound(self):
        order_data = self.create_order()
        order_data[0]['user'] = '131231'

        serializer = OrderSerializer(data=order_data[0])

        self.assertFalse(serializer.is_valid())

        self.assertEqual(set(serializer.errors), set(['user', 'order']))
