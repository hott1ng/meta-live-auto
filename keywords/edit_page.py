from keywords.base import BasePage


class EditPage(BasePage):
    add_product_button = '//button/span[text()=" 产品"]'
    add_script_button = '//button/span[text()=" 话术"]'
    # 产品话术保存按钮
    script_save_button = '//div[@class="edit-box"]//button[@class="el-button el-button--primary"]'

    human_name = '//div[@class="title" and text()="{}"]'

    # 进入第二步
    step2_button = '//div[text()="第二步：添加产品"]'

    # 进入第三步
    step3_button = '//div[text()="第三步：设置直播流程"]'

    # 直播间名字
    project_name = '//div[@class="project-title"]'
    def __init__(self, driver):
        super().__init__(driver)

    def step1(self, name):
        self.base_click(self.human_name.format('元悠9'),(2,2))
        logger.info(f'{name}选择成功')

    def step2_add_product(self, text="测试文本测试文本"):
        self.base_click(self.add_product_button, (0, 1))
        self.base_double_click('//div[text()="双击输入话术"]')
        # time.sleep(1)
        self.base_input('//textarea', text)
        self.base_click(self.script_save_button, (1, 1))
        logger.info('添加产品成功')

    def step2_add_script(self,text="测试文本测试文本"):
        self.base_click(self.add_script_button, (0, 1))
        self.base_input('//textarea', text)
        self.base_click(self.script_save_button, (1, 1))
        logger.info('添加话术成功')

    def step3_add_keywords(self):
        pass

    def step3_add_atmosphere(self):
        pass

    def publish(self):
        # 获取直播间名字
        project_name = self.base_find_element(self.project_name).text
        project_name = project_name.strip()
        self.base_click('//*[text()="保存并发布"]', (1, 5))
        self.base_click('//*[text()="继续"]', (1, 3))
        self.base_click('//*[text()="是"]', (1, 3))

        logger.info('发布成功')
        return project_name


    def main(self):
        self.step1('元悠9')
        self.base_click(self.step2_button, (1, 5))
        self.step2_add_product()
        self.base_click(self.step3_button, (1, 5))
        project_name = self.publish()
        return project_name

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    # time.sleep(2)
    aa = EditPage(driver)
    # aa.step2_add_product()
    aa.main()
