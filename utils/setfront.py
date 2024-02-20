import win32gui
from pywinauto import application
import time


def setFront(title='元分身 • 数字人直播'):
    # 获取应用程序的窗口句柄
    hwnd = win32gui.FindWindow(None, title)
    # 通过句柄连接应用程序
    app = application.Application().connect(handle=hwnd)  # 替换为你的应用程序句柄
    # 获取主窗口并将其置顶
    main_window = app.top_window()
    main_window.set_focus()
    main_window.set_focus()

    # 输出句柄值
# setFront()