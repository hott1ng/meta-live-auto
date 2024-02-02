from pywinauto import Desktop

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