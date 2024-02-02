from base import *


class HumanCenterPage(BasePage):

    online_page_tab = '//*[text()="数字人Online "]'
    make_online_button = '//*[text()="制作数字人Online"]'
    allow_replace_human = '//*[text()="可替换背景online"]'
    make_mode_choice = '//*[text()="{}"]'
    human_name_input = '//*[@placeholder="请输入"]'
    timbre_checkbox = '//*[contains(text(),"同时使用")]'
    next_button = '//*[text()="确定"]'




    def enter_online_tab(self):
        self.base_click(self.online_page_tab,(0,1))


    def make_online_human(self, make_mode, human_name):
        self.base_click(self.make_online_button, (0, 1))
        self.base_click(self.allow_replace_human, (0, 1))
        self.base_click(self.make_mode_choice.format(make_mode), (0, 1))
        self.base_input(self.human_name_input, human_name)
        self.base_click(self.timbre_checkbox, (0, 1))
        self.base_click(self.next_button, (0, 1))

    def run(self, human_name,make_mode='新建主播'):

        self.enter_online_tab()
        self.make_online_human(make_mode,human_name)

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    time.sleep(2)
    aa = HumanCenterPage(driver)
    aa.run('123123')

