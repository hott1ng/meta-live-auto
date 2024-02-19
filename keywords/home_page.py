from base import *


class HomePage(BasePage):
    user_info = '//div[@class="right-part"]//div[@class="user-avatar"]/following-sibling::div[@class="user-name"]'

    edit_page_button = '//div[@class="main-app-content"]//span[text()="新建直播"]'

    living_room_list_button = '//div[@class="main-app-content"]//span[text()="直播管理"]'

    human_center_button = '//div[@class="main-app-content"]//span[text()="数字人中心"]'


    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        pass

    def goto_edit_page(self):
        btn = self.driver.find_elements(By.XPATH, self.edit_page_button)[0]
        btn.click()

    def goto_living_room_list(self):
        self.base_click(self.living_room_list_button)

    def goto_human_center(self):
        self.base_click(self.human_center_button)
