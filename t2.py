import win32gui

# 获取应用程序的窗口句柄
hwnd = win32gui.FindWindow(None, '开播控制台')
# hwnd = win32gui.FindWindow(None, '元分身 • 数字人直播')
win32gui.SetForegroundWindow(hwnd)
# 输出句柄值
print(hwnd)
