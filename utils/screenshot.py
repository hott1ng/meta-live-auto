import pyautogui as pyg
from datetime import datetime
import os



def screenshot(name='屏幕截图'):
    current_time = datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    stamptime = current_time.strftime("%H-%M-%S")
    if not os.path.exists(f'log/screenshot/{date}'):
        os.mkdir(f'log/screenshot/{date}')
    pyg.screenshot(f'log/screenshot/{date}/{name+stamptime}.png')

    return f'log/screenshot/{date}/{name+stamptime}.png'


