from keywords.base import BasePage
from keywords.login_page import LoginPage
from datetime import datetime


class HumanCenterPage(BasePage):
    rule_dict = {
        # 数字人中心首页
        'online数字人标签页': '//*[text()="数字人Online "]',
        '数字人Pro标签页': '//*[text()="数字人Pro "]',
        '制作online数字人按钮': '//*[text()="制作数字人Online"]',
        '可替换背景': '//ul/li[text()="可替换背景online"]',
        '不可替换背景': '//ul/li[text()="不可替换背景online"]',

        # 新建界面
        '新建主播': '//div[text()="新建主播"]',
        '使用已有主播': '//div[contains(text(),"已有主播")]',
        '主播名称输入框': '//*[@placeholder="请输入"]',
        '同时复刻形象音色勾选框': '//*[contains(text(),"同时使用")]',
        '选择已有主播下拉框': '//*[@placeholder="请选择主播"]',
        '根据主播名字选择已有主播': '//li/div/span[text()="{}"]',

        '取消': '//*[text()="取消"]',
        '确定': '//*[text()="确定"]',
    }

    def is_in_human_center_page(self):
        if self.base_find_element(self.rule_dict['制作online数字人按钮']):
            return True
        else:
            return False

    # 进入online界面
    def enter_online_tab(self):
        self.base_click(self.rule_dict['online数字人标签页'], (0, 1))

    def enter_pro_tab(self):
        pass

    # 制作online数字人,已位于online数字人界面
    def make_online_human(self, make_mode, human_type, human_name):
        self.base_click(self.rule_dict['制作online数字人按钮'], (0, 2))
        self.base_click(self.rule_dict[make_mode], (0, 1))
        self.base_click(self.rule_dict[human_type], (0, 1))
        self.base_input(self.rule_dict['主播名称输入框'], human_name)
        self.base_click(self.rule_dict['同时复刻形象音色勾选框'], (0, 1))
        self.base_click(self.rule_dict['确定'], (0, 1))

    def run(self, human_name, make_mode='新建主播'):
        self.enter_online_tab()
        self.make_online_human(make_mode, human_name)

    def main(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        hunman_name = 'online数字人主流程数字人' + timestamp
        self.enter_online_tab()
        import random
        make_mode = random.choice(['可替换背景', '不可替换背景'])
        human_type = random.choice(['新建主播', '使用已有主播'])
        self.make_online_human(make_mode, human_type, hunman_name)



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    time.sleep(2)
    aa = HumanCenterPage(driver)
    aa.main()
