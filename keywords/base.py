import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from loguru import logger
import dotenv
import time


class BasePage:
    user_info_button = ('By.XPATH', '//div[@role="button"]/div[@class="user-name"]')
    dropdown_button = ('By.XPATH', '//div[@class="dropdown-btn-item"]')

    def __init__(self, driver: webdriver.Chrome):
        dotenv.load_dotenv()
        self.driver = driver
        self.ac = ActionChains(self.driver)

    def base_find_element(self, path):
        return self.driver.find_element(By.XPATH, path)

    def base_click(self, path, args=(0, 0)):
        front_wait = args[0]
        behind_wait = args[1]

        time.sleep(front_wait)

        self.base_find_element(path).click()

        time.sleep(behind_wait)

    def base_input(self, path, text):
        self.base_find_element(path).send_keys(text)

    def base_clear(self, path):
        self.base_find_element(path).clear()

    def base_dropdown(self):
        self.base_click(self.user_info_button)
        time.sleep(1)
        self.base_click(self.dropdown_button)

    def base_double_click(self, path):
        ele = self.base_find_element(path)
        self.ac.double_click(ele).perform()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    aa = BasePage(driver)
    aa.base_dropdown()
