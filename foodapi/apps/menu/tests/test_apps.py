from menu.apps import MenuConfig
from .base_file import BaseTestCase


class MenuConfigTest(BaseTestCase):
    def test_apps(self):
        self.assertEqual(MenuConfig.name, 'menu')
