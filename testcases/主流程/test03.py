import time
from keywords.login_page import LoginPage
from keywords.edit_page import EditPage
from keywords.home_page import HomePage
from keywords.project_page import ProjectPage
from keywords.living_page import LivingPage
from keywords.human_center_page import HumanCenterPage
from keywords.create_online_page import CreateOnlinePage
from utils import app,system
import pytest

class Test03:

    def setup_class(self):
        self.driver = app.start_app()
        app.setFront()


    def test_1(self):
        CreateOnlinePage(self.driver).main()

if __name__ == '__main__':
    pytest.main(["-vs", "test_03.py"])