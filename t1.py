import time
from utils.listening import start_listening
import pytest
import threading

if __name__ == '__main__':
    threading.Thread(target=start_listening).start()
    while True:
        pytest.main(["-vs", "testcases/主流程/test02.py"])
        time.sleep(5)