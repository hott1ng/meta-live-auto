import time

from keywords.login_page import LoginPage
from keywords.edit_page import EditPage
from keywords.home_page import HomePage
from utils import app
import time
from selenium import webdriver


class Test01:
    def setup_method(self):
        self.driver = app.base_connect_app()
        # self.page = LoginPage(driver)

    def test_logout(self):
        time.sleep(3)
        self.page = HomePage(self.driver)
        self.page.base_logout()
