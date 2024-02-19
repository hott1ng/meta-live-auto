import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from loguru import logger
import dotenv
import time
from utils.setfront import setFront


class BasePage(object):
    user_info_button = '//div[@class="right-part"]//div[@class="user-avatar"]/following-sibling::div[@class="user-name"]'
    dropdown_button = '//div[@class="dropdown-btn-item"]'

    def __init__(self, driver: webdriver.Chrome):
        dotenv.load_dotenv()
        self.driver = driver
        self.ac = ActionChains(self.driver)

    def base_find_element(self, path):
        if self.base_wait(path):
            return self.driver.find_element(By.XPATH, path)


    # 单击
    def base_click(self, path, args=(0, 0)):
        front_wait = args[0]
        behind_wait = args[1]

        time.sleep(front_wait)

        self.base_find_element(path).click()

        time.sleep(behind_wait)

    # 输入框输入文本
    def base_input(self, path, text):
        self.base_find_element(path).send_keys(text)

    # 清空输入框
    def base_clear(self, path):
        self.base_find_element(path).clear()

    # 退出登录
    def base_logout(self):
        setFront()
        self.base_click(self.user_info_button)
        time.sleep(1)
        self.base_click(self.dropdown_button)

    # 双击
    def base_double_click(self, path):
        ele = self.base_find_element(path)
        self.ac.double_click(ele).perform()

    def base_wait(self, path):
        for i in range(20):
            try:
                if not self.driver.find_element(By.XPATH, path):
                    time.sleep(1)
                else:
                    return True
            except:
                # print(f"找不到{path}")
                time.sleep(1)
        return False


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    aa = BasePage(driver)
    aa.base_logout()
