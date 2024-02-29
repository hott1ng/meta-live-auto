import random

from base import *
from utils import app, system
import time
import os
from dotenv import load_dotenv


class CreateOnlinePage(BasePage):
    rule_dict = {
        # 新建界面第一步
        '选择性别': '//span[text()="{}"]',  # 男  女  其他
        '场景名称输入框': '//span[text()="形象(场景)名称"]//ancestor::div/input[@placeholder="请输入"]',

        # 新建界面第二步
        '上传训练视频': '//div[text()="训练视频"]/ancestor::div[@class="train-video"]//div[@class="upload"]',
        '上传透明通道视频': '//div[text()="对应的透明通道视频"]/ancestor::div[@class="train-video"]//div[@class="upload"]',
        '上传头像': '//*[@class="cover-avatar"]//div[@class="avatar ex-form-item-warn"]',

        # 选取头像封面和头像界面
        '生成封面图': '//div[@class="generate"]',

        # 新建界面第三步
        '上传协议': '//*[text()="上传协议"]',
        '认证方法下拉框': '//div[@class="el-input__content"]',
        '下拉框选择护照': '//span[text()="护照"]',
        '真实姓名输入框': '//*[text()="真实姓名"]/ancestor::div[@class="el-input__wrapper"]//input[@class="el-input__inner" and @placeholder="请输入"]',
        '证件号码输入框': '//*[text()="证件号码"]/ancestor::div[@class="el-input__wrapper"]//input[@class="el-input__inner" and @placeholder="请输入"]',
        '身份证人像面上传按钮': '//div[text()="人像面"]/ancestor::div[@class="placeholder"]',
        '身份证国徽面上传按钮': '//div[text()="国徽面"]/ancestor::div[@class="placeholder"]',
        '护照上传按钮': '//div[text()="含照片面"]/ancestor::div[@class="placeholder"]',

        '下载模板': '',
        '重新上传': '',

        '删除协议': 'use[*|href="#ex-shanchu"]',

        # 提交界面
        '要求多选框': '//div[@class="el-checkbox-group submit-checkbox"]/label',
        '隐私协议勾选框': '//footer//label//span[@class="el-checkbox__inner"]',
        '确定提交': '//*[text()="确定提交"]',

        # 通用
        '确定': '//*[text()="确定"]',
        '取消': '//*[text()="取消"]',
        '上一步': '//*[text()="上一步"]',
        '下一步': '//*[text()="下一步"]',
        '保存': '//*[text()="保存"]',
        '提交': '//*[text()="提交"]',

    }

    # sex_button = '//*[text()="{}"]'
    # scene_input = '//div[@class="el-form-item is-required asterisk-left ex-form-item"]//*[@placeholder="请输入"]'
    # next_step_button = '//*[text()="下一步"]'
    #
    # avatar_button = '//*[text()="封面图"]'
    #
    # create_avatar_button = '//*[text()="生成封面图"]'
    #
    # confirm_button = '//*[text()="确定"]'
    #
    # upload_info = '//*[text()="上传协议"]'
    #
    # prefix_checkbox = '//*[text()="认证方法"]'
    #
    # photo1_button = '//*[text()="人像面"]'
    # photo2_button = '//*[text()="国徽面"]'
    #
    # checkbox_list = '//label'
    #
    # submit_button = '//*[text()="提交"]'
    #
    # agree_button = '//footer//label/span/span'
    #
    # ok_button = '//*[text()="确定提交"]'

    def __init__(self, driver):
        super().__init__(driver)
        load_dotenv()
        self.video1 = os.getenv('video1')
        self.video2 = os.getenv('video2')
        self.pdf = os.getenv('pdf')
        self.photo1 = os.getenv('photo1')
        self.photo2 = os.getenv('photo2')

    def step1(self, scene_name):
        self.base_click(self.rule_dict['选择性别'].format('男'))
        self.base_input(self.rule_dict['场景名称输入框'], scene_name)
        self.base_click(self.rule_dict['下一步'], (0, 1))

    def step2(self, path1, path2):
        uploadbutton = self.driver.find_elements(By.XPATH, '//*[text()="点击上传"]')

        uploadbutton[0].click()
        time.sleep(3)
        system.base_upload(path1)

        uploadbutton[1].click()
        time.sleep(3)
        system.base_upload(path2)

        self.base_click(self.rule_dict['上传头像'], (15, 1))
        self.base_click(self.rule_dict['生成封面图'], (1, 10))
        self.base_click(self.rule_dict['确定'], (1, 10))
        self.base_click(self.rule_dict['下一步'], (0, 1))

    def step3(self, path, photo1, photo2, version=1):
        self.base_click(self.rule_dict['上传协议'], (1, 1))
        system.base_upload(path)

        if version == 1:
            self.base_click(self.rule_dict['身份证人像面上传按钮'], (1, 1))
            system.base_upload(photo1)

            self.base_click(self.rule_dict['身份证国徽面上传按钮'], (1, 1))

            system.base_upload(photo2)




        else:
            self.base_click(self.rule_dict['认证方法下拉框'], (1, 1))
            self.base_click(self.rule_dict['下拉框选择护照'], (1, 1))

            self.base_click(self.rule_dict['护照上传按钮'], (1, 1))
            system.base_upload(photo1)

        self.base_input(self.rule_dict['真实姓名输入框'], '测试')
        self.base_input(self.rule_dict['证件号码输入框'], '111111111111111111')
        # input_list = self.driver.find_elements(By.XPATH, '//*[@placeholder="请输入"]')
        # input_list[0].send_keys('测试')
        # input_list[1].send_keys('111111111111111111')
        self.base_click(self.rule_dict['提交'], (1, 1))

        checkbox_list = self.base_find_elements(self.rule_dict['要求多选框'])
        for i in checkbox_list[:-1]:
            i.click()

        self.base_click(self.rule_dict['隐私协议勾选框'])
        self.base_click(self.rule_dict['确定提交'], (0, 10))

    def run(self, scence_name):

        self.step1(scence_name)
        self.step2(self.video1, self.video2)
        self.step3(self.pdf, self.photo1, self.photo2, version=2)

    def main(self):
        scence_name = 'online数字人主流程场景'
        self.step1(scence_name)
        self.step2(self.video1, self.video2)
        self.step3(self.pdf, self.photo1, self.photo2, version=2)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    aa = CreateOnlinePage(driver)
    aa.run('123')
