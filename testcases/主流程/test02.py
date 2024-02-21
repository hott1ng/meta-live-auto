import time
from keywords.login_page import LoginPage
from keywords.edit_page import EditPage
from keywords.home_page import HomePage
from keywords.project_page import ProjectPage
from keywords.living_page import LivingPage
from utils import app,system
import pytest


class Test02:
    def setup_class(self):
        self.driver = app.start_app()
        app.setFront()

    def setup_method(self):
        self.driver = app.connect_app()
        # self.driver = app.start_app()
        # app.setFront()
        # self.page = LoginPage(driver)


    @pytest.mark.skip
    def test_login(self):
        page = LoginPage(self.driver)
        page.login_pwd()
        driver = app.connect_app()
        page = HomePage(driver)
        title = page.base_find_element('//*[contains(text(),"欢迎")]')
        assert title is not None

    # @pytest.mark.skip
    def test_main(self):
        try:
            page = LoginPage(self.driver)
            page.login_pwd()
            self.driver = app.connect_app()


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
            app.switch_to(self.driver, '//*[text()="关注互动"]')
            # self.driver.switch_to.window(window)

            page = LivingPage(self.driver)
            page.main()
        except:
            system.screenshot()

    # def testquit(self):
    #     print(111)

    def teardown_class(self):
        # while True:
        # self.driver = app.base_start_app()
        # setFront()

        # switch_to(self.driver, '//*[text()="模板中心"]')

        # teardown不会触发setup
        driver = app.start_app()
        app.setFront()
        page = HomePage(driver)
        try:
            page.logout()

        except:
            app.check_quit(driver)
        #
        #     if not check_quit(driver):
        #         driver = app.base_start_app()
        #         setFront()
        #
        #         page = HomePage(driver)
        #         page.base_logout()


            # if check_quit(self.driver):
            #     break
            # time.sleep(5)

