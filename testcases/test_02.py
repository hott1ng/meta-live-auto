import pytest


class Test01:
    def test01(self):
        raise TimeoutError
        # self.page = LoginPage(driver)
    # def test02(self):
    #     print(111)
    def teardown_class(self):
        print("运行了")

if __name__ == '__main__':
    import os
    print(os.getcwd())
    pytest.main(["-vs", "test_02.py"])