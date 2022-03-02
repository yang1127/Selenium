'''
import unittest

from selenium import webdriver
from Base.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage(unittest.TestCase):

    def test_01_login(self):
        """登录用例"""
        # 打开浏览器
        driver = webdriver.Chrome()
        # 加载网页
        driver.get("https://panjiachen.github.io/vue-element-admin")
        # 点击登录按钮
        driver.find_element(By.XPATH, "//*[@id='app']/div/form/button").click()


    def test_02_select_file(self):
        """导出zip文件"""
        # 先登录
        # 打开浏览器
        global driver
        driver = webdriver.Chrome()
        # 加载网页
        driver.get("https://panjiachen.github.io/vue-element-admin")
        # 点击登录按钮
        driver.find_element(By.XPATH, "//*[@id='app']/div/form/button").click()

        # 智能等待
        driver.implicitly_wait(2)

        # 再查询

        # 文本部分匹配-包含：//标签名[contains(text(), 部分文本内容)]
        driver.find_element(By.XPATH, "//span[contains(text(),'Zip')]").click()  # 先找到Zip目录
        driver.find_element(By.XPATH, "//span[contains(text(),'Export Zip')]").click()  # 再找到Export Zip目录

        # 再Export Zip中，输入文件名称
        driver.find_element(By.XPATH, "//input[@class='el-input__inner' and @placeholder = '请输入文件名(默认file)']").send_keys("0")

        # 导出相应文件
        driver.find_element(By.XPATH, "//span[contains(text(),'导出 Zip')]").click()

    def test_03_select_file(self):
        """下拉框选择"""
        # 先登录
        # 打开浏览器
        global driver
        driver = webdriver.Chrome()
        # 加载网页
        driver.get('http://sahitest.com/demo/selectTest.htm')

        # 实例化Select
        s1 = Select(driver.find_element(By.ID, 's1Id'))

        # 1、通过下标选择
        # s1.select_by_index(1)  # 选择选项：o1

        # 2、通过value值
        # s1.select_by_value("o2")  # 选择value="o2"

        # 3、通过t文本
        s1.select_by_visible_text("o3")  # 选择text="o3"的值
    '''

"""涉及框架：有框架，先进入框架，<frame></frame>"""
'''
eg：menu-frame框架优先 + main-frame框架
1、先进menu-frame框架
driver.switch_to.frame("menu-frame")  

2、再进main-frame框架，前提：先出menu-frame框架
# 出menu-frame框架
driver.switch_to.default_content()
# 进入main-frame框架
driver.switch_to.frame("main-frame") 
'''

'''
不唯一的场景需要怎么搞？

# 定位一组删除按钮
del_list = driver.find_elements(By.XPATH, "//img[@src='images/'images/icon_trash.gif']")
if len(del_list) >= 1:
    del_list[0].click()


windows 自带弹窗：
1、alert:确定按钮
2、confirm:确定 + 取消按钮
3、prompt:确定 + 取消按钮 + 输入框


# 处理windows自带弹窗
ale = driver.switch_to.alert
# 获取文本
print(ale.text)
ale.accept()
'''

'''
windows 自带弹窗：
1、alert:确定按钮
2、confirm:确定 + 取消按钮
3、prompt:确定 + 取消按钮 + 输入框
'''