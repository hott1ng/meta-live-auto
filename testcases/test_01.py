from keywords.login_page import LoginPage
from keywords.edit_page import EditPage

from selenium import webdriver


class Test01:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        # options.binary_location = os.getenv("BINARY_LOCATION")
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(options=options)
        self.page = LoginPage(driver)

    def test_login(self):
        print(self.page.driver.window_handles)
        self.page.login_pwd()
        self.page.switch_to(self.driver.window_handles[0])
        print(self.driver.window_handles)
        self.page = EditPage(self.driver)
        title = self.page.find_element_by_xpath('//*[contains(text(),"欢迎")]')
        assert title is not None
