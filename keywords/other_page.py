from datetime import datetime
import random
from utils import app, system
from dotenv import load_dotenv
from keywords.base_page import BasePage
import os
from selenium.webdriver.common.by import By
from loguru import logger
import dotenv
import time
from utils import app

dotenv.load_dotenv()


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
        '已有主播下拉框': '//*[@placeholder="请选择主播"]',
        '根据主播名字选择已有主播': '//li/div/span[text()="{}"]',
        '主播下拉框人头': '//li[@class="el-select-dropdown__item"]'

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
        self.base_click(self.rule_dict['选择性别'].format(random.choice(['男','女','其他'])))
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
        if human_type == '使用已有主播':
            self.base_click(self.rule_dict['已有主播下拉框'], (0, 1))
            check_list = self.base_find_elements(self.rule_dict['主播下拉框人头'])
            check_list[0].click()
        else:
            self.base_input(self.rule_dict['主播名称输入框'], human_name)
        self.base_click(self.rule_dict['同时复刻形象音色勾选框'], (0, 1))
        self.base_click(self.rule_dict['确定'], (0, 1))

    def main(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        hunman_name = 'online数字人主流程数字人' + timestamp
        self.enter_online_tab()

        make_mode = random.choice(['可替换背景', '不可替换背景'])
        # human_type = random.choice(['新建主播', '使用已有主播'])
        human_type = random.choice(['新建主播'])
        self.make_online_human(make_mode, human_type, hunman_name)
        scence_name = 'online数字人主流程场景' + timestamp
        self.step1(scence_name)
        self.step2(self.video1, self.video2, make_mode)
        self.step3(self.pdf, self.photo1, self.photo2, version=2)


class EditPage(BasePage):
    # add_product_button = '//button/span[text()=" 产品"]'
    # add_script_button = '//button/span[text()=" 话术"]'
    # # 产品话术保存按钮
    # script_save_button = '//div[@class="edit-box"]//button[@class="el-button el-button--primary"]'
    #
    # human_name = '//div[@class="title" and text()="{}"]'
    #
    # # 进入第二步
    # step2_button = '//div[text()="第二步：添加产品"]'
    #
    # # 进入第三步
    # step3_button = '//div[text()="第三步：设置直播流程"]'
    #
    # # 直播间名字
    # project_name = '//div[@class="project-title"]'

    rule_dict = {
        '添加产品按钮': '//button/span[text()=" 产品"]',
        '添加话术按钮': '//button/span[text()=" 话术"]',
        '产品话术保存按钮': '//div[@class="edit-box"]//button[@class="el-button el-button--primary"]',
        '数字人名字': '//div[@class="title" and text()="{}"]',
        '进入第二步按钮': '//div[text()="第二步：添加产品"]',
        '进入第三步按钮': '//div[text()="第三步：设置直播流程"]',
        '直播间名字': '//div[@class="project-title"]',
        '背景列表': '//div[@class="background"]//div[@class="el-col el-col-8 is-guttered"]',
        '装饰列表': '//div[2]//div[@class="deco-item"]/img',

        '首次新增关键词互动': '//div[@class="btn-group"]/button[1]',
        '非首次新增关键词互动': '//div[@class="add-icon"]',

        '规则输入框': '//div[@class="key-word"]//textarea',
        '话术输入框': '//div[@class="key-word"]//div[@class="input-content"]',
        '关键词互动保存按钮': '//div[@class="key-word"]//*[text()="保存"]',
        '关键词回复方下拉框': '//div[@class="key-word"]//span[@class="input-prefix" and text()="回复方"]',
        '关键词打断方式下拉框': '//div[@class="key-word"]//span[@class="input-prefix" and text()="打断方式"]',

        '选择回复方为': '//div[@aria-hidden="true"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[text()="{}"]',
        '选择打断方式为': '//div[@aria-hidden="false"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[text()="{}"]',

        '氛围引导按钮列表': '//span[@class="el-switch__core"]',
    }

    def __init__(self, driver):
        super().__init__(driver)

    def step1_select_human(self, name):
        self.base_click(self.rule_dict['数字人名字'].format('元悠9'), (2, 2))
        logger.info(f'{name}选择成功')

    def step1_select_background(self):
        background_list = self.base_find_elements(self.rule_dict['背景列表'])
        self.base_click(random.choice(background_list))

    def step1_select_decoration(self):
        background_list = self.base_find_elements(self.rule_dict['装饰列表'])
        self.base_click(random.choice(background_list))

    def step2_add_product(self, text="测试文本测试文本"):
        self.base_click(self.rule_dict['添加产品按钮'], (0, 1))
        self.base_double_click('//div[text()="双击输入话术"]')
        # time.sleep(1)
        self.base_input('//textarea', text)
        self.base_click(self.rule_dict['产品话术保存按钮'], (1, 1))
        logger.info('添加产品成功')

    def step2_add_script(self, text="测试文本测试文本"):
        self.base_click(self.rule_dict['添加话术按钮'], (0, 1))
        self.base_input('//textarea', text)
        self.base_click(self.rule_dict['产品话术保存按钮'], (1, 1))
        logger.info('添加话术成功')

    def step3_add_keywords(self, replyer, mode, rules, text):
        # 第一次新增规则
        if self.base_find_element(self.rule_dict['首次新增关键词互动']):
            self.base_click(self.rule_dict['首次新增关键词互动'])
        else:
            self.base_click(self.rule_dict['非首次新增关键词互动'])

        if replyer == '助播':
            self.base_click(self.rule_dict['关键词回复方下拉框'])
            self.base_click(self.rule_dict['选择回复方为'].format(replyer))

        if mode == '立即':
            self.base_click(self.rule_dict['关键词打断方式下拉框'])
            self.base_click(self.rule_dict['选择打断方式为'].format(replyer))

        self.base_input(self.rule_dict['规则输入框'], rules)
        self.base_input(self.rule_dict['话术输入框'], text)
        self.base_click(self.rule_dict['关键词保存按钮'], (1, 1))

    def step3_start_atmosphere(self, index: list):
        btn_list = self.base_find_elements(self.rule_dict['氛围引导按钮列表'])
        for i in index:
            self.base_click(btn_list[i], (1, 1))

    def publish(self):
        # 获取直播间名字
        project_name = self.base_find_element(self.project_name).text
        project_name = project_name.strip()
        self.base_click('//*[text()="保存并发布"]', (1, 5))
        self.base_click('//*[text()="继续"]', (1, 3))
        self.base_click('//*[text()="是"]', (1, 3))

        logger.info('发布成功')
        return project_name

    def get_project_name(self):
        project_name = self.base_find_element(self.rule_dict['直播间名字']).text
        return project_name

    def main(self):
        self.step1('元悠9')
        self.base_click(self.step2_button, (1, 5))
        self.step2_add_product()
        self.base_click(self.step3_button, (1, 5))
        project_name = self.publish()
        return project_name


class HomePage(BasePage):
    user_info = '//div[@class="right-part"]//div[@class="user-avatar"]/following-sibling::div[@class="user-name"]'

    edit_page_button = '//div[@class="main-app-content"]//span[text()="新建直播"]'

    living_room_list_button = '//div[@class="main-app-content"]//span[text()="直播管理"]'

    human_center_button = '//div[@class="main-app-content"]//span[text()="数字人中心"]'

    rule_dict = {
        '用户信息': '//div[@class="right-part"]//div[@class="user-avatar"]/following-sibling::div[@class="user-name"]',
        '模板列表': '//div[@class="el-row is-justify-space-between"]/div',
        '直播管理按钮': '//div[@class="main-app-content"]//span[text()="直播管理"]',
        '新建直播按钮': '//div[@class="main-app-content"]//span[text()="新建直播"]',
        '数字人中心按钮': '//div[@class="main-app-content"]//span[text()="数字人中心"]',
    }

    def __init__(self, driver):
        super().__init__(driver)

    # 退出登录
    def logout(self):
        app.setFront()
        self.base_click(self.user_info_button)
        time.sleep(1)
        self.base_click(self.dropdown_button)

    def goto_edit_page(self):
        btn = self.driver.find_elements(By.XPATH, self.edit_page_button)[0]
        btn.click()

    def goto_living_room_list(self):
        self.base_click(self.living_room_list_button)

    def goto_human_center(self):
        self.base_click(self.human_center_button)


class HumanCenterPage(BasePage):
    rule_dict = {
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

        '取消': '//*[text()="取消"]',
        '确定': '//*[text()="确定"]',

    }

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

    def run(self, human_name, make_mode='新建主播'):
        self.enter_online_tab()
        self.make_online_human(make_mode, human_name)

    def main(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        hunman_name = 'online数字人主流程数字人' + timestamp
        self.enter_online_tab()
        import random
        make_mode = random.choice(['可替换背景', '不可替换背景'])
        human_type = random.choice(['新建主播', '使用已有主播'])
        self.make_online_human(make_mode, human_type, hunman_name)


class LivingPage(BasePage):
    spider_platform = '//div[@class="panel-header"]//span[text()="直播平台"]'

    platform_text = '//ul/li/span[contains(text(),"{}")]'

    platform_url = '//input[@placeholder="请输入"]'

    start_spider_button = '//span[text()="开启"]'

    # 智能互动按钮
    ai_button = '//div[text()="智能互动"]/following-sibling::div/span'

    ai_tab = '//div[text()="智能互动"]'

    def __init__(self, driver):
        super().__init__(driver)

    def back_to_living_page(self, livingroom_name):
        pass

    def start_spider(self, platform, url):
        self.base_click(self.spider_platform, (1, 1))
        self.base_click(self.platform_text.format(platform), (1, 1))
        self.base_input(self.platform_url, url)
        self.base_click(self.start_spider_button, (1, 1))
        self.base_click(self.ai_button, (1, 1))
        self.base_click(self.ai_tab, (1, 1))
        logger.info('开启爬虫成功')

    def mon_answer(self):
        for i in range(60):
            try:
                if self.driver.find_element(By.XPATH, '//div[@class="reply-tooltip" and @style="display: none;"]'):
                    time.sleep(1)
            except:
                logger.info('爬虫正常使用')
                return
        logger.info('爬虫异常，一分钟内未触发过')

    def shutdown_living(self):
        self.base_click('//*[text()="结束直播"]', (1, 1))
        self.base_click('//*[text()="是"]', (1, 1))

    def main(self):
        self.start_spider('抖音', 'https://live.douyin.com/33430193638')
        self.mon_answer()
        self.shutdown_living()


class LoginPage(BasePage):
    rule_dict = {
        '验证码登录tab': '//*[text()="验证码登录"]',
        '密码登录tab': '//*[text()="密码登录"]',
        '手机号输入框': '//*[@aria-hidden="false"]//input[@placeholder="请输入手机号"]',
        '密码输入框': '//*[@aria-hidden="false"]//input[@placeholder="请输入密码"]',
        '验证码输入框': '//*[@aria-hidden="false"]//input[@placeholder="请输入验证码"]',
        '登录按钮': '//*[text()="登录"]',
        '协议勾选框': '//*[@class="el-checkbox__inner"]',
        '更新按钮': '//*[text()="立即更新"]',
    }

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

    def back_to_login_page(self):
        pass

    def login_pwd(self):
        self.base_click(self.rule_dict['密码登录tab'], (0, 2))
        self.base_input(self.rule_dict['手机号输入框'], self.phone_number)
        self.base_input(self.rule_dict['密码输入框'], self.password)
        self.base_click(self.rule_dict['协议勾选框'], (0, 2))
        self.base_click(self.rule_dict['登录按钮'], (0, 7))

    def login_sms(self):
        pass


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

    def wait_publish(self, name, times=3):
        self.base_click(self.refresh_button, (0, 4))
        for i in range(times):
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

        self.base_click(self.start_living_button, (2, 2))

        app.switch_to(self.driver, '//*[text()="关注互动"]')

    def edit(self):
        pass


class RetryPage():

    def back_to_human_center_page(self, driver):
        # 从登录界面返回数字人中心界面
        LoginPage(driver).login_pwd()
