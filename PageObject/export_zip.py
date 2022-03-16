from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

from Base.base_page import BasePage


import time

class Export_Zip(BasePage):

    """元素定位"""
    submit_zip = (By.XPATH, "//span[contains(text(),'Zip')]")
    submit_export_zip = (By.XPATH, "//span[contains(text(),'Export Zip')]")
    file_name = (By.XPATH, "//input[@class='el-input__inner' and @placeholder = '请输入文件名(默认file)']")
    find_zip = (By.XPATH, "//span[contains(text(),'导出 Zip')]")

    """元素动作"""
    def select_file(self, file_value):
        self.click(self.submit_zip)
        self.click(self.submit_export_zip)
        self.filename_by_value(self.file_name, file_value)
        self.click(self.find_zip)



