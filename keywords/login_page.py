import os
from base import *
import time


class LoginPage(BasePage):
    # 切换验证码登录tab
    sms_tab_button = '//*[text()="验证码登录"]'
    # 切换密码登录tab
    pwd_tab_button = '//*[text()="密码登录"]'
    # 可见的手机号输入框
    phone_number_input = '//*[@aria-hidden="false"]//input[@placeholder="请输入手机号"]'
    # 密码输入框
    pwd_input = '//*[@aria-hidden="false"]//input[@placeholder="请输入密码"]'
    # 验证码输入框
    sms_input = '//*[@aria-hidden="false"]//input[@placeholder="请输入验证码"]'
    # 获取验证码按钮
    get_sms_button = '//*[text()="获取验证码"]'
    # 登录按钮
    login_button = '//*[text()="登录"]'
    # 协议按钮
    agreement_button = '//*[@class="el-checkbox__inner"]'
    # 更新按钮
    update_button = '//*[text()="立即更新"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.phone_number = os.getenv('PHONE')
        self.password = os.getenv('PASSWORD')

    def goto_login_page(self):
        pass

    def login_pwd(self):
        self.base_click(self.pwd_tab_button, (0, 2))
        self.base_input( self.phone_number_input, self.phone_number)
        self.base_input( self.pwd_input, self.password)
        self.base_click(self.agreement_button, (0, 2))
        self.base_click(self.login_button, (0, 7))

    def login_sms(self):
        pass


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    aa = LoginPage(driver)
    aa.login_pwd()
