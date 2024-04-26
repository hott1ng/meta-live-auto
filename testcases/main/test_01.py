import time
from keywords.login_page import LoginPage
from keywords.edit_page import EditPage
from keywords.home_page import HomePage
from utils import app
from utils.app import setFront
from selenium import webdriver


class Test01:
    def setup_method(self):
        self.driver = app.base_connect_app()
        setFront()
        # self.page = LoginPage(driver)

    def test_login(self):
        self.page = LoginPage(self.driver)
        print(self.page.driver.window_handles)
        self.page.login_pwd()
        # self.page.switch_to(self.driver.window_handles[0])
        driver = app.base_connect_app()
        print(driver.window_handles)
        self.page = HomePage(driver)
        title = self.page.base_find_element('//*[contains(text(),"欢迎")]')
        print(title.text)
        assert title is not None


    # def teardown_method(self):
    #     self.page.base_logout()
