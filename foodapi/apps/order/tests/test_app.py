from order.apps import OrderConfig
from .base_file import BaseTestCase


class OrderConfigTest(BaseTestCase):
    def test_apps(self):
        self.assertEqual(OrderConfig.name, 'order')
