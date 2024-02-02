from base import *

class ProjectPage(BasePage):

    tr_name = '//div[text()={}]'

    # 通过项目名定位
    name_to_button = (By.XPATH,'//*[text()="{}"]/ancestor::tr//span[text()="{}"]')


    def __init__(self, driver):
        super().__init__(driver)


    def publish(self):
        self.click()

    def goto_live(self):
        btn = (self.name_to_button[0],self.name_to_button[1].format('自定义产品顺序测试', '开播'))
        self.click(*btn)

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