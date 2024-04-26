import pytest
from keywords.other_page import *


class TestShouYe:

    def setup_class(self):
        self.driver = app.connect_app()

    def setup_method(self):
        pass

    def teardown_method(self):
        self.driver.get('app://localhost/home')

    def test_moban_01(self):
        page = HomePage(self.driver)
        page.base_click(page.base_find_elements(page.rule_dict['模板列表'])[0])

        page = EditPage(self.driver)
        page.base_click(page.rule_dict['进入第三步按钮'])
        project_name = page.get_project_name()
        page.publish()

        page = ProjectPage(self.driver)
        page.wait_publish(project_name, 12)
        page.goto_live(project_name)

        page = LivingPage(self.driver)
        page.shutdown_living()

    def test_xinjianzhibo_01(self):
        page = HomePage(self.driver)
        page.base_click(page.rule_dict['新建直播按钮'])

        page = EditPage(self.driver)
        assert page.base_find_element(page.rule_dict['进入第二步按钮']) != None
