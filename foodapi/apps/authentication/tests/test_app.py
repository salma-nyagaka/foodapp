from authentication.apps import AuthenticationConfig
from .base_file import BaseTestCase


class AuthenticationConfigTest(BaseTestCase):
    def test_apps(self):
        self.assertEqual(AuthenticationConfig.name, 'authentication')
