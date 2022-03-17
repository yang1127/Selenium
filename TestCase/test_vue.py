import time
import logging
import allure
import pytest

from selenium import webdriver
from tenacity import retry

from PageObject.login_page import LoginPage

from PageObject.export_zip import Export_Zip


# class Test_Login_Vue(unittest.TestCase): # unittest
from common.excel_util import read_excel


class Test_Login_Vue():

    # 前置
    def setup_class(self) -> None:
        self.log = logging.getLogger()  # 初始化log
        self.log.info("======打开浏览器======")  # 加入log
        # 打开浏览器
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver

    # 失败重试
    @retry
    def test_01_login(self):
        self.log.info("======登录模块======")  # 加入log
        # 在报告中加入用例的名称和描述
        allure.dynamic.title("登录测试用例")
        allure.dynamic.description("登录测试用例的一些描述")
        login = LoginPage(self.driver)  # 实例化对象
        login.login_vue()

    '''
    @pytest.mark.parametrize("file_name_info", read_excel("/Users/yangzhiqi/PycharmProjects/Selenium/Data/data.xlsx", "export"))
    def test_02_file(self, file_name_info):
        try:
            self.log.info("======下载模块======")  # 加入log
            # print(file_name_info)
            index, case_name, file_name, is_exe, result = file_name_info

            # 在报告中加入用例的名称和描述
            allure.dynamic.title(case_name)
            allure.dynamic.description(case_name)

            login = LoginPage(self.driver)  # 实例化对象
            login.login_vue()

            driver.implicitly_wait(2)  # 元素还未生成或者页面还没有加载出来就执行了定位操作,等会

            file = Export_Zip(self.driver)
            # file.select_file("0")

            file.select_file(file_name)
        except Exception as e:
            self.log.info("======下载不成功，错误截图======")  # 加入log
            # print("代码出现异常就会执行")
            # 获得一个时间戳的字符串
            str_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            # 图片路径
            image_path = "./images/"+str_time+".png"
            # 错误截图
            self.driver.save_screenshot(image_path)
            # 读取图片信息并且加入到allure报告中
            # allure.attach(body=文件流, name=文件名称, attachment_type=附件的格式)
            with open(image_path, mode='rb') as f:
                stream = f.read()
                allure.attach(body=stream, name=image_path, attachment_type=allure.attachment_type.PNG)
    '''
    
    def teardown_class(self) -> None:
        time.sleep(2)
        self.driver.close()
        self.log.info("======关闭浏览器======")  # 加入log


'''
if __name__ == '__main__':
    Test_Login_Vue().test_01_login()
'''


