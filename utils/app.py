from selenium import webdriver


def base_start_app(path):
    driver = webdriver.Chrome(path)
    return driver


def base_connect_app():
    options = webdriver.ChromeOptions()
    # options.binary_location = os.getenv("BINARY_LOCATION")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver