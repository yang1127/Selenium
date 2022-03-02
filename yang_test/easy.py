'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

page = driver.get("https://www.baidu.com/")
'''

'''
Selenium元素定位方式主要有以下八种：
1、id 定位 -- find_element_by_id()
2、name 定位 -- find_element_by_name()
3、class name 定位 -- find_element_by_class_name()
4、tag name 定位 -- find_element_by_tag_name()
5、link text 定位 -- find_element_by_link_text()
6、partial link text 定位 -- find_element_by_partial_link_text()
7、xpath 定位 -- find_element_by_xpath()
8、css selector定位 -- find_element_by_css_selector()
'''

# 1、id 定位 -- find_element_by_id() -- 3.6版本之前支持，之后 find_element(By.ID, "id值")
# driver.find_element(By.ID, "kw").send_keys("selenium")

# 2、name 定位
# driver.find_element(By.NAME, "wd").send_keys("selenium")


# 3、class name 定位
# driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("selenium")

# 4、tag name 标签名称定位，可能会不成功，标签中东西多，不唯一
# driver.find_element(By.TAG_NAME, "input").send_keys("selenium")

# 5、link text 链接的全部文字定位
# driver.find_element(By.LINK_TEXT, "hao123").click()

# 6、partial link text 链接的部分文字定位
# driver.find_element(By.PARTIAL_LINK_TEXT, "hao").click()

# 7、xpath 定位
# 7.1 绝对路径 -- 用一个/开头
# 写法："//span[@class='soutu-btn']/input"

# 7.2 相对路径 -- 用两个//开头
# 简单方法：直接F12，copy获取
# driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("selenium")

'''
# 常用的几种方法：
"//*[@id='kw']"
"//*[@name='wd']"
"//input[@class='s_ipt']"
"//span[@class='soutu-btn']/input"
"//form[@id='form']/span/input"
"//input[@id='kw' and @name='wd']"
'''
# 相对路径：//form/div/input
# driver.find_element(By.XPATH, "//form/span/input").send_keys("selenium")

# 相对路径+索引：//form/div[1]/input
# driver.find_element(By.XPATH, "//form/span[1]/input").send_keys("selenium")

# 相对路径+属性：//input[@placeholder="Username"]
# driver.find_element(By.XPATH, "//input[@id='kw' and @name='wd']").send_keys("selenium")

# 8、css selector 定位  -- CSS表达式式，可F12获取
# driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium")

'''
# 测试下网易邮箱登录
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

page = driver.get("https://www.jianshu.com/sign_in")

# 帐号、秘密
driver.find_element(By.XPATH, "//*[@id='session_email_or_mobile_number']").send_keys("18702970462")
driver.find_element(By.XPATH, "//*[@id='session_password']").send_keys("yyy1536520643")

# 登录
driver.find_element(By.XPATH, "//*[@id='sign-in-form-submit-btn']").click()
'''

# 测试下Vue登录
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

page = driver.get("https://panjiachen.github.io/vue-element-admin")

# 帐号、秘密
# driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[2]/div/div/input']").send_keys("admin")
# driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[3]/div/div/input").send_keys("111111")

# 登录 Vue
driver.find_element(By.XPATH, "//*[@id='app']/div/form/button").click()
