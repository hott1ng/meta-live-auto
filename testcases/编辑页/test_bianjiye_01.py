from utils import app
from keywords.other_page import *

class TestBianJiYe:

    def setup_class(self):
        self.driver = app.start_app()

    def setup_method(self):
        pass

    def test_smoke(self):
        HomePage(self.driver).base_click(HomePage.rule_dict['新建直播按钮'])

        page = EditPage(self.driver)
        page.step1_select_human('元悠9')
        page.step1_select_background()
        page.step1_select_decoration()

        page.base_click(page.rule_dict['进入第二步按钮'])
        page.step2_add_product()

        page.base_click(page.rule_dict['进入第三步按钮'])


