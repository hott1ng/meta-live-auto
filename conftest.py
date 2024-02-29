import pytest
from utils import system,app
from datetime import datetime


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call, video_flag=False):
    current_time = datetime.now()

    # 获取钩子方法的调用结果
    out = yield
    testcases_name = item.function.__doc__
    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    # print(testcases_name)
    if report.when == 'call':
        if report.outcome != 'passed':
            system.screenshot(current_time)

    if video_flag:
        system.get_front_30video(current_time)


# 每次操作前连接到客户端
@pytest.fixture(scope='function', autouse=False)
def connect_client():
    app.connect_app()