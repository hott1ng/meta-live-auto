from keywords import human_center_page,create_online_page,base_page
from selenium import webdriver
import time

if __name__ == '__main__':
    with open('num.txt', 'r') as f:
        num = int(f.read().split('=')[-1])
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    print('实例化')
    time.sleep(2)
    driver.get('app://localhost/center')
    aa = human_center_page.HumanCenterPage(driver)
    time.sleep(1)
    aa.enter_online_tab()

    for i in range(100):
        try:
            num+=1
            time.sleep(2)
            print('进入')
            aa = human_center_page.HumanCenterPage(driver)
            aa.run(f'伟直播护照_主播{num}')
            bb = create_online_page.CreateOnlinePage(driver)
            bb.run(f'伟直播护照_音色{num}')
            with open('num.txt', 'w')as f:
                f.write(f'num={num}')
        except Exception as e:
            print('未知错误',e)
            driver.get('app://localhost/center')
            time.sleep(10)
            aa = human_center_page.HumanCenterPage(driver)
            time.sleep(1)
            aa.enter_online_tab()



