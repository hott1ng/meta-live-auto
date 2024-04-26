import time
from utils import app
import pytest
import threading

if __name__ == '__main__':
    threading.Thread(target=app.start_listening).start()
    while True:
        pytest.main(["-v", "testcases/主流程/test_main.py"])
        time.sleep(5)