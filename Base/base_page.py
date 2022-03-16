import logging

from selenium import webdriver

from selenium.webdriver.common.by import By

# 基础层，所有的方法不能写死
class BasePage:

    # 每个页面都要写 __init__
    # 由于页面对象的类都要调用基础的类，所以在这块构造，即每个页面都继承了 __init__
    def __init__(self, driver):
        self.log = logging.getLogger()  # 初始化log
        self.driver = driver

    '''
    # 打开浏览器 - 写代码时打开，运行关闭
    def open_browser(self):
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
    '''

    # 加载网页
    def get_page(self, url):
        self.driver.get(url)

    # 定位元素
    def locate_element(self, args):
        return self.driver.find_element(*args)  # 要点击等，需要return返回

    # 设置值 - eg：帐号、密码
    def send_keys(self, args, value):
        self.locate_element(args).send_keys(value)

    # 单击
    def click(self, args):
        self.locate_element(args).click()

     # 输入名称
    def filename_by_value(self, args, value):
        self.locate_element(args).send_keys(value)
