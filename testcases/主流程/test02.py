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


class Test02:
    def setup_method(self):
        # self.driver = app.base_connect_app()
        self.driver = app.base_start_app()
        setFront()
        # self.page = LoginPage(driver)


    # @pytest.mark.skip
    def test_login(self):
        page = LoginPage(self.driver)
        page.login_pwd()
        driver = app.base_connect_app()
        page = HomePage(driver)
        title = page.base_find_element('//*[contains(text(),"欢迎")]')
        assert title is not None

    # @pytest.mark.skip
    def test_main(self):
        # switch_to(self.driver, '//*[text()="模板中心"]')
        page = HomePage(self.driver)
        page.goto_edit_page()
        time.sleep(10)

        page = EditPage(self.driver)
        # 返回直播间名称
        project_name = page.main()
        # project_name = '新直播2024021923'
        page = ProjectPage(self.driver)
        page.wait_publish(project_name)
        page.goto_live(name=project_name)
        time.sleep(5)
        switch_to(self.driver, '//*[text()="关注互动"]')
        # self.driver.switch_to.window(window)

        page = LivingPage(self.driver)
        page.main()

    # def testquit(self):
    #     print(111)

    def teardown_class(self):
        # while True:
        # self.driver = app.base_start_app()
        # setFront()

        # switch_to(self.driver, '//*[text()="模板中心"]')

        # teardown不会触发setup
        driver = app.base_start_app()
        setFront()
        try:
            page = HomePage(driver)
            page.base_logout()

        except:

            if not check_quit(driver):
                driver = app.base_start_app()
                setFront()

                page = HomePage(driver)
                page.base_logout()


            # if check_quit(self.driver):
            #     break
            # time.sleep(5)

