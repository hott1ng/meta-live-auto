from keywords.login_page import LoginPage

class RetryPage():

    def back_to_human_center_page(self, driver):
        # 从登录界面返回数字人中心界面
        LoginPage(driver).login_pwd()