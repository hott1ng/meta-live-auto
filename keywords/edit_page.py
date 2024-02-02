from base import *


class EditPage(BasePage):
    add_product_button = '//button/span[text()=" 产品"]'
    add_script_button = '//button/span[text()=" 话术"]'
    # 产品话术保存按钮
    script_save_button = '//div[@class="edit-box"]//button[@class="el-button el-button--primary"]'

    human_name = '//div[@class="title" and text()="{}"]'

    def __init__(self, driver):
        super().__init__(driver)

    def step1(self, name):
        self.click(self.human_name.format('元悠9'))
        logger.info(f'{name}选择成功')

    def step2_add_product(self):
        self.click(self.add_product_button, (0, 1))
        self.double_click('//div[text()="双击输入话术"]')
        # time.sleep(1)
        self.input('//textarea', '123')
        self.click(self.script_save_button, (1, 1))
        logger.info('添加产品成功')

    def step2_add_script(self):
        self.click(self.add_script_button, (0, 1))
        self.input('//textarea', '123')
        self.click(self.script_save_button, (1, 1))
        logger.info('添加话术成功')

    def step3_add_keywords(self):
        pass

    def step3_add_atmosphere(self):
        pass

    def publish(self):
        self.click('//*[text()="第三步：设置直播流程"]', (1, 5))
        self.click('//*[text()="保存并发布"]', (1, 5))
        self.click('//*[text()="继续"]', (1, 3))
        self.click('//*[text()="是"]', (1, 3))
        logger.info('发布成功')


    def main(self):
        self.step1('元悠9')
        self.step2_add_product()
        self.publish()

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    # time.sleep(2)
    aa = EditPage(driver)
    # aa.step2_add_product()
    aa.main()
