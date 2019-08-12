# 对话框的定位
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
# 点击登录链接
driver.find_element_by_name("tj_login").click()
# 通过二次定位找到用户名输入框
div=driver.find_element_by_class_name("tang-content").find_element_by_name("userName")
div.send_keys("username")
# 输入登录密码
driver.find_element_by_name("password").send_keys("password")
# 点击登录
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
driver.quit()
# 本例中并没有用到新方法，唯一的技巧是用到了二次定位，这个技巧