from selenium import webdriver


# 基础层，所有的方法不能写死
class BasePage:

    # 打开浏览器
    def open_browser(self):
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver

    # 加载网页
    def get_page(self, url):
        self.driver.get(url)

    # 定位元素
    def locate_element(self, args):
        return self.driver.find_element(*args)

    # 设置值
    def send_keys(self, args, value):
        self.locate_element(args).send_keys(value)

    # 单击
    def click(self, args):
        self.locate_element(args).click()
