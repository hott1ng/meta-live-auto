import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_car_data():
    url = 'https://souapi.pcauto.com.cn/auto/api/v2/pc/choose_car/result'
    output = {}

    for i in range(1,2):
        data = {"rl":["5","6","8","3"],"sort":"","pageSize":10,"pageNo":i}
        response = requests.post(url,json=data)
        response_json = response.json()['result']['data']
        for i in response_json:
            name = i['groupName']
            id_ = i['serialGroupId']
            output.update({name:id_})

    with open('car.json','w')as f:
        f.write(json.dumps(output, ensure_ascii=False))

def get_price(car_id, phone_number):
    base_url = f'https://price.pcauto.com.cn/sg{car_id}/price.html'
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.find_element(By.XPATH,'//*[contains(text(),"获取底价")]').click()


    driver.find_element(By.XPATH,'//*[@placeholder="请输入您的称呼（如李先生）"]').send_keys('李先生')
    driver.find_element(By.XPATH,'//*[@placeholder="请输入您的手机号"]').send_keys(phone_number)
    driver.find_element(By.XPATH,'//*[@class="submit-button"]').click()

    driver.find_element(By.XPATH,'//*[contains(text(),"您可以跳过")]').click()
    driver.find_element(By.XPATH,'//*[contains(text(),"跳过")]').click()


def run(phone_number):
    with open('car.json', 'r') as f:
        car_info = f.read()
        car_info = json.loads(car_info)
    for k,v in car_info.items():
        try:
            get_price(v,phone_number)
        except:
            print(f'{k}未知错误')

if __name__ == '__main__':
    phone_number = input("输入手机号")
    run(phone_number)