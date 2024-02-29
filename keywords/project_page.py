from keywords.base import BasePage


class ProjectPage(BasePage):
    tr_name = '//div[text()={}]'

    # 通过项目名定位
    name_to_button = '//*[text()="{}"]/ancestor::tr//span[text()="{}"]'

    name_to_status = '//*[text()="{}"]/ancestor::tr/td//div[text()=" 待开播"]'

    refresh_button = '//*[text()="刷新"]'

    start_living_button = '//*[text()="开始直播"]'

    def __init__(self, driver):
        super().__init__(driver)

    def back_to_project_page(self):
        pass

    def publish(self):
        self.base_click()

    def wait_publish(self, name):
        self.base_click(self.refresh_button, (0, 4))
        for i in range(3):
            if self.base_find_element(self.name_to_status.format(name)):
                return
            else:
                self.base_click(self.refresh_button, (0, 4))
        raise Exception('等待合成超时')


    def goto_live(self, name=None):
        if name:
            btn = self.name_to_button.format(name, '开播')
            self.base_click(btn)
        else:
            # 开播第一个
            self.driver.find_elements(By.XPATH, '//span[text()="开播"]')[0].click()

        self.base_click(self.start_living_button,(2,2))

    def edit(self):
        pass


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    # time.sleep(2)
    aa = ProjectPage(driver)
    aa.goto_live()
