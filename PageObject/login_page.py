from selenium.webdriver.common.by import By

from Base.base_page import BasePage


class LoginPage(BasePage):

    current_url = "https://panjiachen.github.io/vue-element-admin"

    """页面元素定位"""
    # 无 帐号、密码输入
    # username_loc = (By.NAME, "username")
    # password_loc = (By.NAME, "password")
    submit_login = (By.XPATH, "//*[@id='app']/div/form/button")

    """元素动作"""
    def login_vue(self):
        # self.open_browser()
        self.get_page(self.current_url)
        self.click(self.submit_login)

    '''
    def login_vue(self, username="admin", password="111111"):
        self.open_browser()
        self.get_page(self.current_url)
        self.send_keys(self.username_loc, username)
        self.send_keys(self.password_loc, password)
        self.click(self.submit_login)
    '''
