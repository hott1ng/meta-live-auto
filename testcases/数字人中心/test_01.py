import pytest
from keywords.other_page import *


class Test01:

    def setup_class(self):
        self.driver = app.start_app()
        app.setFront()


    def test01(self):
        CreateOnlinePage(self.driver).main()

