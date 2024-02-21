import random

from base import *
from utils import app,system
import time
import os
from dotenv import load_dotenv


class CreateOnlinePage(BasePage):
    sex_button = '//*[text()="{}"]'
    scene_input = '//div[@class="el-form-item is-required asterisk-left ex-form-item"]//*[@placeholder="请输入"]'
    next_step_button = '//*[text()="下一步"]'

    avatar_button = '//*[text()="封面图"]'

    create_avatar_button = '//*[text()="生成封面图"]'

    confirm_button = '//*[text()="确定"]'

    upload_info = '//*[text()="上传协议"]'

    prefix_checkbox = '//*[text()="认证方法"]'

    photo1_button = '//*[text()="人像面"]'
    photo2_button = '//*[text()="国徽面"]'

    checkbox_list = '//label'

    submit_button = '//*[text()="提交"]'

    agree_button = '//footer//label/span/span'

    ok_button = '//*[text()="确定提交"]'

    def __init__(self, driver):
        super().__init__(driver)
        load_dotenv()
        self.video1 = os.getenv('video1')
        self.video2 = os.getenv('video2')
        self.pdf = os.getenv('pdf')
        self.photo1 = os.getenv('photo1')
        self.photo2 = os.getenv('photo2')

    def step1(self, scene_name):
        self.base_click(self.sex_button.format('男'))
        self.base_input(self.scene_input, scene_name)
        self.base_click(self.next_step_button, (0, 1))

    def step2(self, path1, path2):
        uploadbutton = self.driver.find_elements(By.XPATH, '//*[text()="点击上传"]')

        uploadbutton[0].click()
        time.sleep(3)
        system.base_upload(path1)

        uploadbutton[1].click()
        time.sleep(3)
        system.base_upload(path2)

        self.base_click(self.avatar_button, (15, 1))
        self.base_click(self.create_avatar_button, (1, 10))
        self.base_click(self.confirm_button, (1, 10))
        self.base_click(self.next_step_button, (0, 1))

    def step3(self, path, photo1, photo2, version=1):
        self.base_click(self.upload_info, (1, 1))
        system.base_upload(path)

        if version==1:
            self.base_click(self.photo1_button, (1, 1))
            system.base_upload(photo1)

            self.base_click(self.photo2_button, (1, 1))

            system.base_upload(photo2)




        else:
            self.base_click(self.prefix_checkbox,(1,1))
            self.base_click('//span[text()="护照"]',(1,1))

            self.base_click('//*[text()="含照片面"]', (1, 1))
            system.base_upload(photo1)


        input_list = self.driver.find_elements(By.XPATH, '//*[@placeholder="请输入"]')
        input_list[0].send_keys('测试')
        input_list[1].send_keys('111111111111111111')
        self.base_click(self.submit_button, (1, 1))

        checkbox_list = self.driver.find_elements(By.XPATH, self.checkbox_list)
        for i in checkbox_list[:-1]:
            i.click()

        self.base_click(self.agree_button)
        self.base_click(self.ok_button, (0, 10))

    def run(self, scence_name):



        self.step1(scence_name)
        self.step2(self.video1, self.video2)
        self.step3(self.pdf,self.photo1,self.photo2, version=2)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    aa = CreateOnlinePage(driver)
    aa.run('123')
