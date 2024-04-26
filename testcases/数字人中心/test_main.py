import pytest
from keywords.other_page import *
import time
from dotenv import load_dotenv
import os

class TestMain:
    def setup_class(self):
        self.driver = app.connect_app()
        app.setFront()
        load_dotenv()

    # 制作可替换背景
    def test_01(self):
        timestamp = str(int(time.time()))
        page = HumanCenterPage(self.driver)
        page.enter_online_tab()
        page.make_online_human('可替换背景', '新建主播', '自动化数字人' + timestamp)

        page = CreateOnlinePage(self.driver)
        page.step1('自动化场景' + timestamp)
        page.step2(os.getenv('TRAIN_VIDEO'), os.getenv('_VIDEO'), '可替换背景')
        page.step3(os.getenv('RULES'), os.getenv('PHOTO_1'), os.getenv('PHOTO_2'), 1)
        # assert



    # 制作不可替换背景
    def test_02(self):
        timestamp = str(int(time.time()))
        page = HumanCenterPage(self.driver)
        page.enter_online_tab()
        page.make_online_human('可替换背景', '新建主播', '自动化数字人' + timestamp)

        page = CreateOnlinePage(self.driver)
        page.step1('自动化场景' + timestamp)
        page.step2(os.getenv('TRAIN_VIDEO'), os.getenv('_VIDEO'), '不可替换背景')
        page.step3(os.getenv('RULES'), os.getenv('PHOTO_1'), os.getenv('PHOTO_2'), 1)
        # assert
