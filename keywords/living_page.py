from base import *
import time



class LivingPage(BasePage):
    spider_platform = '//div[@class="panel-header"]//span[text()="直播平台"]'

    platform_text = '//ul/li/span[contains(text(),"{}")]'

    platform_url = '//input[@placeholder="请输入"]'

    start_spider_button = '//span[text()="开启"]'

    # 智能互动按钮
    ai_button = '//div[text()="智能互动"]/following-sibling::div/span'
    def __init__(self, driver):
        super().__init__(driver)

    def start_spider(self, platform, url):
        self.base_click(self.spider_platform, (1, 1))
        self.base_click(self.platform_text.format(platform), (1, 1))
        self.base_input(self.platform_url, url)
        self.base_click(self.start_spider_button, (1, 1))
        self.base_click(self.ai_button, (1, 1))
        logger.info('开启爬虫成功')

    def mon_answer(self):
        for i in range(3):
            try:
                if self.base_find_element('//div[@class="reply-state"]'):
                    logger.info('爬虫正常使用')
                    return
                else:
                    time.sleep(1)
            except:
                logger.info('爬虫异常，正在重新开启')
        logger.info('爬虫异常，一分钟内未触发过')
    def shutdown_living(self):
        self.base_click('//*[text()="结束直播"]', (1, 1))
        self.base_click('//*[text()="是"]', (1, 1))

    def main(self):
        self.start_spider('抖音', 'https://live.douyin.com/33430193638')
        self.mon_answer()
        self.shutdown_living()




if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    aa = LivingPage(driver)
    aa.start_spider('抖音', 'https://live.douyin.com/33430193638')