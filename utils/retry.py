import time
from screenshot import screenshot
from listening import start_listening
import threading

def check_quit(driver):
    # 在直播间卡住
    if len(driver.window_handles) != 0:
        screenshot()
        driver.close()
        t1 = threading.Thread(target=start_listening)
        t1.start()
        # start_listening()
        time.sleep(5)
        return False
    else:
        return True

