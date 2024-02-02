from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import dotenv
import os
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
import pandas as pd


class Keywords:

    def __init__(self):
        dotenv.load_dotenv()
        options = webdriver.ChromeOptions()
        # options.binary_location = os.getenv("BINARY_LOCATION")
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)
        self.action = ActionChains(self.driver)
        # 读取 Excel 文件
        df = pd.read_excel('各国语言.xlsx', sheet_name='Sheet1')

        # 获取 A 列和 B 列的值
        column_a = df['名称']
        column_b = df['试听文本']
        self.language = {}

        # 遍历 A 列和 B 列的值
        for index, value_a in column_a.items():
            self.language.update({value_a.strip(): column_b[index]})

        self.Four_List = ['韩语', '日语']
        self.Thfi_List = ['普通话', '粤语', '台湾普通话', '四川话', '上海话', '陕西话', '东北话', '河南话', '天津话']
        self.Sehu_List = ['波斯语', '印地语', '阿拉伯语']
        self.Eihu_List = ['乌尔都语', '克罗地亚语', '威尔士语', '孟加拉语', '捷克语', '波兰语', '老挝语', '斯洛伐克语',
                          '斯瓦希里语', '祖鲁语']
        self.Nihu_List = ['乌克兰语', '乌兹别克语', '俄语', '冰岛语', '加利西亚语', '匈牙利语', '土耳其语',
                          '塞尔维亚语', '爱尔兰语', '立陶宛语', '芬兰语', '葡萄牙语', '保加利亚语', '哈萨克语',
                          '普什图语', '索马里语', '泰米尔语']
        self.OnTh_List = ['丹麦语', '希腊语', '德语', '瑞典语', ' 缅甸语', '高棉语', '荷兰语', '蒙古语', '马耳他语',
                          '亚美尼亚语', '阿尔巴尼亚语',
                          '僧伽罗语', '英语（EN）', '英语（US）', '马来语', '泰语', '越南语', '菲律宾语', '印尼语',
                          '西班牙语', '意大利语', '法语']



    def download(self):
        # self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="tab-password"]').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[3]/div/input').clear()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div[3]/div/input').send_keys(
            os.getenv("PHONE"))
        self.driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys(os.getenv("PASSWORD"))
        self.driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/div/div/div/div[3]/label/span[1]/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/div/div/div/div[4]/button/span/span').click()

    def create_room(self, language_type, text):
        self.driver.get('app://localhost/management')
        # self.driver.implicitly_wait(5)
        time.sleep(8)
        # money = self.driver.find_element(By.XPATH, '//div[@class="activated-state"]/preceding-sibling::div[@class="right-expires"]/div[@class="item"][2]/text()')


        self.driver.find_element(By.XPATH, '//*[text()="新建直播"]').click()
        time.sleep(8)
        element = self.driver.find_element(By.XPATH, '//*[@id="anchor-item-731"]/div[1]/img')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # 改直播间名
        self.driver.find_element(By.XPATH, '//div[@class="project-title"]/*').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div/input[@placeholder="请输入"]').clear()
        self.driver.find_element(By.XPATH, '//div/input[@placeholder="请输入"]').send_keys(f'{language_type}')
        self.driver.find_element(By.XPATH, '//*[text()="确定"]').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="decorate__container"]/div[1]/div[3]/div[2]').click()

        time.sleep(2)
        # 点击主播音色设置
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]/div[2]/div/div[1]/div/div[1]/div/div[2]/div[1]').click()

        time.sleep(2)
        # 选择语言
        language = self.driver.find_element(By.XPATH, f'//*/span[contains(text(),"{language_type}")]')
        # try:
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", language)
        # self.driver.implicitly_wait(5)
        # time.sleep(2)
        self.driver.find_element(By.XPATH, f'//*/span[contains(text(),"{language_type}")]').click()
        # except:
        #     self.driver.execute_script("arguments[0].scrollIntoView();", language)
        #     # self.driver.implicitly_wait(5)
        #     time.sleep(2)
        #     language.click()

        timbre = self.driver.find_element(By.XPATH, '//*/span[contains(text(),"甜美女声")]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", timbre)
        # self.driver.implicitly_wait(5)
        time.sleep(2)
        timbre.click()

        self.driver.find_element(By.XPATH, '//*/button[contains(text(),"确定")]').click()

        # 添加产品话术
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]/div[2]/div/div[1]/div/div[1]/div/div[1]/button[1]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="decorate__container"]/div[1]/div[3]/div[2]').click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[text()="未命名产品"]').click()
        # self.driver.find_element(By.XPATH, '//*/button/span[text()=" 话术"]').click()
        element = self.driver.find_elements(By.XPATH, '//*/div[contains(text(),"双击输入话术")]')[-1]
        self.action.double_click(element).perform()

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*/textarea').send_keys(f'{text}')
        self.driver.find_element(By.XPATH, '//*[@id="decorate__container"]//span[text()="保存"]').click()

        time.sleep(2)
        # 进入第三步
        self.driver.find_element(By.XPATH, '//*[@id="decorate__container"]/div[1]/div[5]/div[2]').click()
        time.sleep(5)

        # 点击助播音色
        self.driver.find_element(By.XPATH, f'//*[text()="助播音色"]').click()
        time.sleep(2)
        # 选择助播语言
        language = self.driver.find_element(By.XPATH, f'//*/span[contains(text(),"{language_type}")]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", language)
        # self.driver.implicitly_wait(5)
        time.sleep(2)
        language.click()

        timbre = self.driver.find_element(By.XPATH, '//*/span[contains(text(),"激情男声")]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", timbre)
        time.sleep(2)
        # self.driver.implicitly_wait(5)
        timbre.click()

        self.driver.find_element(By.XPATH, '//*/button[contains(text(),"确定")]').click()

        self.driver.find_element(By.XPATH, '//*/span[text()="新增规则"]').click()

        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="输入多个关键词，用逗号分隔"]').send_keys(
            'A')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="请输入话术"]').send_keys(
            f'{text}')

        # 改变回复方
        self.change_answer(1, '主播', '立即')
        # 插入变量
        self.add_insert_variable(1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="key-word"]//*[text()="保存"]').click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*/span[text()="规则"]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="输入多个关键词，用逗号分隔"]').send_keys(
            'B')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="请输入话术"]').send_keys(
            f'{text}')
        # 改变回复方
        self.change_answer(1, '助播', '立即')
        # 插入变量
        self.add_insert_variable(1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="key-word"]//*[text()="保存"]').click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*/span[text()="规则"]').click()

        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="输入多个关键词，用逗号分隔"]').send_keys(
            'C')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="请输入话术"]').send_keys(
            f'{text}')

        # 改变回复方
        self.change_answer(1, '主播', '立即')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="key-word"]//*[text()="保存"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*/span[text()="规则"]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="输入多个关键词，用逗号分隔"]').send_keys(
            'D')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="edit-region__reply"]//*[@placeholder="请输入话术"]').send_keys(
            f'{text}')

        # 改变回复方
        self.change_answer(1, '助播', '立即')
        self.driver.find_element(By.XPATH,
                                 '//*[@id="decorate__container"]//div[@class="key-word"]//*[text()="保存"]').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, '//*[text()="保存并发布"]').click()
        # self.driver.implicitly_wait(5)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*/button[text()="继续"]').click()
        time.sleep(5)
        # self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//*/button[text()="是"]').click()

        time.sleep(8)

    def change_answer(self, type, answer, mode):
        type_ = {
            1: 'edit-region__reply',
            2: 'mood-guide-script-list'
        }

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//span[text()="回复方"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, f'//div[@aria-hidden="false"]//span[text()="{answer}"]').click()

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//span[text()="打断方式"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, f'//div[@aria-hidden="false"]//span[text()="{mode}"]').click()

    def add_insert_variable(self, type):
        type_ = {
            1: 'edit-region__reply',
            2: 'mood-guide-script-list'
        }

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//span[text()="打断方式"]').click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]//span[text()="立即"]').click()

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//div[text()="插入变量"]').click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]//li[text()="用户昵称"]').click()

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//div[text()="插入变量"]').click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]//li[text()="在线人数"]').click()

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//div[text()="插入变量"]').click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]//li[text()="总观看人数"]').click()

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//div[text()="插入变量"]').click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]//li[text()="礼物名称"]').click()

        self.driver.find_element(By.XPATH,
                                 f'//*[@id="decorate__container"]//div[@class="{type_[type]}"]//div[text()="插入变量"]').click()
        time.sleep(0.1)
        self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]//li[text()="实时时间"]').click()


    def check(self, types, text):

        length = len(text)
        if types in self.Thfi_List:
            ans = length * 60 // 350
            # print(ans)
        elif types in self.Four_List:
            ans = length * 60 // 400
            # print(ans)
        elif types in self.Sehu_List:
            ans = length * 60 // 700
            # print(ans)
        elif types in self.Eihu_List:
            ans = length * 60 // 800
            # print(ans)
        elif types in self.Nihu_List:
            ans = length * 60 // 900
        elif types in self.OnTh_List:
            ans = length * 60 // 1000

        return ans


    def run(self):
        for k, v in self.language.items():
            try:
                self.create_room(k, v)
            except:
                print(k, v,'失败')


if __name__ == '__main__':
    meta = Keywords()
    meta.run()
