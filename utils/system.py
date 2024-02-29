import time

from pywinauto import Desktop
import pyautogui as pyg

import os
import shutil
from datetime import datetime


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


def close_update_window():
    app = Desktop(backend='win32')
    dlg = app['yuan-live-test 安装']
    dlg.set_focus()
    dlg.child_window(title="运行 yuan-live-test(&R)", class_name="Button").click_input()
    dlg.child_window(title="完成(&F)", class_name="Button").click_input()


def close_error_window():
    app = Desktop(backend='win32')
    dlg = app['Error']
    dlg.set_focus()
    dlg.child_window(title="确定", class_name="Button").click_input()


def screenshot(current_time, name='屏幕截图'):
    date = current_time.strftime("%Y-%m-%d")
    timestamp = current_time.strftime("%H-%M-%S")
    if not os.path.exists(f'log/screenshot/{date}'):
        os.mkdir(f'log/screenshot/{date}')
    pyg.screenshot(f'log/screenshot/{date}/{name + timestamp}.png')

    return f'log/screenshot/{date}/{name + timestamp}.png'


def get_front_30video(current_time):

    pyg.hotkey('win', 'alt', 'g')

    # 源文件夹路径
    source_dir = r"C:\Users\user\Videos\Captures"
    # 目标文件夹路径，您可以根据需要更改
    date = current_time.strftime("%Y-%m-%d")
    timestamp = current_time.strftime("%H-%M-%S")
    target_dir = f".\\log\\video\\{date}"

    # 确保目标文件夹存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_dir):
        # 检查文件是否以"元分身"开头且是视频文件（例如，扩展名为.mp4或.avi）
        # if filename.startswith("元分身") and filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv')):
        # 获取文件的完整路径
        if 'desktop' in filename:
            continue
        source_path = os.path.join(source_dir, filename)

        # 创建时间戳作为新文件名

        new_filename = f"{timestamp}.{filename.split('.')[-1]}"  # 保持原始文件扩展名

        # 创建新文件的完整路径
        target_path = os.path.join(target_dir, new_filename)

        # 移动并重命名文件
        shutil.move(source_path, target_path)



if __name__ == '__main__':
    get_front_30video()
