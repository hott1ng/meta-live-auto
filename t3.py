from utils.app import base_connect_app
from selenium.webdriver.common.by import By


driver = base_connect_app()
print(driver.current_window_handle)
handle = driver.window_handles[0]

driver.switch_to.window(handle)
print(driver.current_window_handle)
print(driver.find_element(By.XPATH,"//*[text()='商品互动']"))