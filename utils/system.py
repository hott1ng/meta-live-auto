from pywinauto import Desktop
import pyautogui as pyg
from datetime import datetime
import os


def base_upload(filename):
    app = Desktop(backend='win32')
    # 选中文件上传的窗口

    dlg = app["打开"]
    dlg.set_focus()
    # upload_input = dlg.child_window( control_type='Edit')  # 根据实际情况找到文件上传输入框
    # upload_input.click_input()
    # dlg.child_window(title="截图").click_input()
    dlg.type_keys(filename)
    dlg.type_keys('{ENTER}')


def screenshot(name='屏幕截图'):
    current_time = datetime.now()
    date = current_time.strftime("%Y-%m-%d")
    stamptime = current_time.strftime("%H-%M-%S")
    if not os.path.exists(f'log/screenshot/{date}'):
        os.mkdir(f'log/screenshot/{date}')
    pyg.screenshot(f'log/screenshot/{date}/{name + stamptime}.png')

    return f'log/screenshot/{date}/{name + stamptime}.png'