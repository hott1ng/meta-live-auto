
from pywinauto import Desktop


try:
    app = Desktop(backend='win32')
    if app.window(title='Error').exists():
        dlg = app['Error']
        dlg.print_control_identifiers()
        dlg.set_focus()
        dlg.child_window(title="确定", class_name="Button").click_input()
        print(111)
except:
    print(222)