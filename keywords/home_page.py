from base import *


class HomePage(BasePage):
    user_info = '//div[@class="right-part"]//div[@class="user-avatar"]/following-sibling::div[@class="user-name"]'


    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        pass
