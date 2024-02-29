from base import *


class HumanCenterPage(BasePage):
    rule_dict = {
        # 数字人中心首页
        'online数字人标签页': '//*[text()="数字人Online "]',
        '数字人Pro标签页': '//*[text()="数字人Pro "]',
        '制作online数字人按钮': '//*[text()="制作数字人Online"]',

        # 新建界面
        '可替换背景online数字人选项': '//*[text()="可替换背景online"]',
        '不可替换背景online数字人选项': '//*[text()="不可替换背景online"]',
        '新建主播': '//div[@class="type-item" and text()="新建主播"]',
        '使用已有主播': '//div[contains(text(),"已有主播")]',
        '主播名称输入框': '//*[@placeholder="请输入"]',
        '同时复刻形象音色勾选框': '//*[contains(text(),"同时使用")]',
        '选择已有主播下拉框': '//*[@placeholder="请选择主播"]',
        '根据主播名字选择已有主播': '//li/div/span[text()="{}"]',

    }

    # pro_page_tab = '//*[text()="数字人Pro "]'
    # make_online_button = '//*[text()="制作数字人Online"]'

    # allow_replace_human = '//*[text()="可替换背景online"]'
    # unallow_replace_human = '//*[text()="不可替换背景online"]'

    make_mode_choice = '//*[text()="{}"]'

    # human_name_input = '//*[@placeholder="请输入"]'
    # timbre_checkbox = '//*[contains(text(),"同时使用")]'
    # new_scene_button = '//div[@class="type-item" and text()="新建主播"]'
    # old_scene_button = '//div[contains(text(),"已有主播")]'

    next_button = '//*[text()="确定"]'
    cancel_button = '//*[text()="取消"]'

    # 进入online界面
    def enter_online_tab(self):
        self.base_click(self.rule_dict['online数字人标签页'], (0, 1))

    def enter_pro_tab(self):
        pass

    # 制作online数字人,已位于online数字人界面
    def make_online_human(self, make_mode, human_name):
        self.base_click(self.make_online_button, (0, 1))
        self.base_click(self.allow_replace_human, (0, 1))
        self.base_click(self.make_mode_choice.format(make_mode), (0, 1))
        self.base_input(self.human_name_input, human_name)
        self.base_click(self.timbre_checkbox, (0, 1))
        self.base_click(self.next_button, (0, 1))

    def run(self, human_name, make_mode='新建主播'):
        self.enter_online_tab()
        self.make_online_human(make_mode, human_name)

    def main(self):
        hunman_name = 'online数字人主流程数字人'
        self.enter_online_tab()
        self.make_online_human('新建主播', hunman_name)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    time.sleep(2)
    aa = HumanCenterPage(driver)
    aa.run('123123')
