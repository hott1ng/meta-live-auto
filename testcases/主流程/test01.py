import time

import pytest

from keywords.login_page import LoginPage
from keywords.edit_page import EditPage
from keywords.home_page import HomePage
from keywords.project_page import ProjectPage
from keywords.living_page import LivingPage
from utils import app
from utils.setfront import setFront
from utils.switch import switch_to
from utils.retry import check_quit
from selenium import webdriver
import pytest


class Test01:
    def setup_method(self):
        # self.driver = app.base_connect_app()
        self.driver = app.base_start_app()
        setFront()
        # self.page = LoginPage(driver)


    @pytest.mark.skip
    def test_login(self):
        self.page = LoginPage(self.driver)
        self.page.login_pwd()
        driver = app.base_connect_app()
        self.page = HomePage(driver)
        title = self.page.base_find_element('//*[contains(text(),"欢迎")]')
        assert title is not None

    @pytest.mark.skip
    def test_main(self):
        # switch_to(self.driver, '//*[text()="模板中心"]')
        self.page = HomePage(self.driver)
        self.page.goto_edit_page()
        time.sleep(10)

        self.page = EditPage(self.driver)
        # 返回直播间名称
        project_name = self.page.main()
        # project_name = '新直播2024021923'
        self.page = ProjectPage(self.driver)
        self.page.wait_publish(project_name)
        self.page.goto_live(name=project_name)
        time.sleep(5)
        switch_to(self.driver, '//*[text()="关注互动"]')
        # self.driver.switch_to.window(window)

        self.page = LivingPage(self.driver)
        self.page.main()

    def test_quit(self):
        print(111)

    def teardown_class(self):
        # while True:
        # self.driver = app.base_start_app()
        # setFront()

        # switch_to(self.driver, '//*[text()="模板中心"]')
        self.page = HomePage(self.driver)
        self.page.base_logout()

            # if check_quit(self.driver):
            #     break
            # time.sleep(5)

