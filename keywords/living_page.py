from base import *
import time



class LivingPage(BasePage):
    spider_platform = '//div[@class="panel-header"]//span[text()="直播平台"]'

    platform_text = '//ul/li/span[contains(text(),"{}")]'

    platform_url = '//input[@placeholder="请输入"]'

    def __init__(self, driver):
        super().__init__(driver)

    def start_spider(self, platform, url):
        self.base_click(self.spider_platform, (1, 1))
        self.base_click(self.platform_text.format(platform), (1, 1))
        self.base_input(self.platform_url, url)
        self.base_click('//span[text()="开启"]', (1, 1))
        logger.info('开启爬虫成功')

    def mon_answer(self):
        while True:

            if self.base_find_element('//div[@class="reply-state"]'):
                logger.info('爬虫正常使用')
                break
            else:
                time.sleep(1)

    def shutdown_living(self):
        self.base_click('//*[text()="结束直播"]', (1, 1))
        self.base_click('//*[text()="是"]', (1, 1))



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    aa = LivingPage(driver)
    aa.start_spider('抖音', 'https://live.douyin.com/33430193638')