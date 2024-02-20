import time
import threading
from selenium import webdriver
from dotenv import load_dotenv
import os
import time

load_dotenv()

def start_listening():
    path = os.getenv("BINARY_LOCATION")
    os.system(f"{path} --remote-debugging-port=9222")


def base_start_app():
    # thread = threading.Thread(target=start_listening)
    # thread.start()
    driver = base_connect_app()
    time.sleep(5)
    return driver


def base_connect_app():
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver

