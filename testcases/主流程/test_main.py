import time
from keywords.other_page import *
from utils import app,system
import pytest


class TestMain:
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

        LoginPage(self.driver).login_pwd()

        self.driver = app.connect_app()


        HomePage(self.driver).goto_edit_page()

        time.sleep(10)
        # 返回直播间名称
        project_name = EditPage(self.driver).main()

        page = ProjectPage(self.driver)


        page.wait_publish(project_name)
        page.goto_live(name=project_name)
        time.sleep(5)
        app.switch_to(self.driver, '//*[text()="关注互动"]')
        # self.driver.switch_to.window(window)

        page = LivingPage(self.driver)
        page.main()

    # def testquit(self):
    #     print(111)

    # def teardown_class(self):
    #     # while True:
    #     # self.driver = app.base_start_app()
    #     # setFront()
    #
    #     # switch_to(self.driver, '//*[text()="模板中心"]')
    #
    #     # teardown不会触发setup
    #     system.close_error_window()
    #     driver = app.start_app()
    #     app.setFront()
    #     page = HomePage(driver)
    #     try:
    #         page.logout()
    #
    #     except:
    #         app.check_quit(driver)
    #     #
    #     #     if not check_quit(driver):
    #     #         driver = app.base_start_app()
    #     #         setFront()
    #     #
    #     #         page = HomePage(driver)
    #     #         page.base_logout()
    #
    #
    #         # if check_quit(self.driver):
    #         #     break
    #         # time.sleep(5)

