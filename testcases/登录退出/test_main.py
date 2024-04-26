from keywords.other_page import *
from utils import app
import pytest


class TestMain:
    def setup_class(self):
        self.driver = app.start_app()
        app.setFront()

    def test_login(self):
        page = LoginPage(self.driver)
        page.login_pwd()

    def test_logout(self):
        page = HomePage(self.driver)
        page.logout()
