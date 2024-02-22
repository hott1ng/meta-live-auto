from selenium import webdriver
from dotenv import load_dotenv
import os
import win32gui
from pywinauto import application
from selenium.webdriver.common.by import By
import time
import threading
from keywords.living_page import LivingPage
from keywords.home_page import HomePage
from utils import system
from pywinauto import Desktop

load_dotenv()


def start_listening():
    path = os.getenv("BINARY_LOCATION")
    os.system(f"{path} --remote-debugging-port=9222")


def start_app():
    thread = threading.Thread(target=start_listening)
    thread.start()
    driver = connect_app()
    time.sleep(5)
    return driver


def connect_app():
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver


def switch_to(driver, path):
    for window in driver.window_handles:
        driver.switch_to.window(window)
        try:
            if driver.find_element(By.XPATH, path):
                return driver
        except:
            pass


def setFront(title='元分身 • 数字人直播'):
    # 获取应用程序的窗口句柄
    hwnd = win32gui.FindWindow(None, title)
    # 通过句柄连接应用程序
    app = application.Application().connect(handle=hwnd)  # 替换为你的应用程序句柄
    # 获取主窗口并将其置顶
    main_window = app.top_window()
    main_window.set_focus()
    main_window.set_focus()


def check_quit(driver):
    """
    失败后大退
    没有找到退出按钮进入该方法

    判断窗口数量
    1.大退后重新启动，返回新的driver
    2.弹出更新
    3.先关闭开播控制台，再走正常登录流程

    """
    # 被error卡住
    app = Desktop(backend='win32')
    if app.window(title='Error').exists():
        system.close_error_window()
    # 在home被卡住
    if len(driver.window_handles) == 1:
        driver.close()
        t1 = threading.Thread(target=start_listening)
        t1.start()
        # start_listening()
        time.sleep(5)
        driver = connect_app()

    # 被更新卡住
    elif len(driver.window_handles) == 2:
        # 待定
        driver = switch_to(driver, '//*[text()="立即更新"]')
        driver.find_element(By.XPATH, '//*[text()="立即更新"]').click()
        time.sleep(60)

        system.close_update_window()

        t1 = threading.Thread(target=start_listening)
        t1.start()
        driver = connect_app()

    # 在直播间被卡住
    elif len(driver.window_handles) == 3:
        driver = switch_to(driver, '//*[text()="结束直播"]')
        page = LivingPage(driver)
        page.shutdown_living()

        driver.close()
        t1 = threading.Thread(target=start_listening)
        t1.start()
        # start_listening()
        time.sleep(5)
        driver = connect_app()

    if driver.current_url == 'app://localhost/home':
        page = HomePage(driver)
        page.logout()
    return driver


if __name__ == '__main__':
    start_listening()
