import time
# import unittest

from selenium import webdriver

from PageObject.login_page import LoginPage

from PageObject.export_zip import Export_Zip


# class Test_Login_Vue(unittest.TestCase): # unittest
class Test_Login_Vue():

    # 前置
    def setup_class(self) -> None:
        # 打开浏览器
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver

    def test_01_login(self):
        login = LoginPage(self.driver)  # 实例化对象
        login.login_vue()

    def test_02_file(self):
        login = LoginPage(self.driver)  # 实例化对象
        login.login_vue()

        driver.implicitly_wait(2)  # 元素还未生成或者页面还没有加载出来就执行了定位操作,等会

        file = Export_Zip(self.driver)
        file.select_file("0")

    def teardown_class(self) -> None:
        time.sleep(5)
        self.driver.quit()



