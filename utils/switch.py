from selenium.webdriver.common.by import By


def switch_to(driver, path):
    for window in driver.window_handles:
        driver.switch_to.window(window)
        try:
            if driver.find_element(By.XPATH, path):
                return driver
        except:
            pass
