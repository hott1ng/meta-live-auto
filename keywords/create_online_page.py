from datetime import datetime
import random
from keywords.base_page import BasePage
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

    }

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

    def step2(self, path1, path2, make_mode):
        self.base_click(self.rule_dict['上传训练视频'], (0, 1))
        system.base_upload(path1)
        time.sleep(3)

        if make_mode == '可替换背景':
            self.base_click(self.rule_dict['上传透明通道视频'], (0, 1))
            system.base_upload(path2)
            time.sleep(3)

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
        for i in checkbox_list:
            i.click()

        self.base_click(self.rule_dict['隐私协议勾选框'])
        self.base_click(self.rule_dict['确定提交'], (0, 10))

    def run(self, scence_name):

        self.step1(scence_name)
        self.step2(self.video1, self.video2)
        self.step3(self.pdf, self.photo1, self.photo2, version=2)

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

    def main(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        hunman_name = 'online数字人主流程数字人' + timestamp
        self.enter_online_tab()

        make_mode = random.choice(['可替换背景', '不可替换背景'])
        human_type = random.choice(['新建主播', '使用已有主播'])
        self.make_online_human(make_mode, human_type, hunman_name)
        scence_name = 'online数字人主流程场景' + timestamp
        self.step1(scence_name)
        self.step2(self.video1, self.video2, make_mode)
        self.step3(self.pdf, self.photo1, self.photo2, version=2)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    aa = CreateOnlinePage(driver)
    aa.main()
