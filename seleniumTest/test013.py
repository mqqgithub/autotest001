# alert/confirm/prompt  处理
'''
webdriver 中处理 JavaScript 所生成的 alert、confirm 以及 prompt 是很简单的。具体思路是使用
switch_to.alert()方法定位到 alert/confirm/prompt。然后使用 text/accept/dismiss/send_keys 按需进行操做。
 text 返回 alert/confirm/prompt 中的文字信息。
 accept 点击确认按钮。
 dismiss 点击取消按钮，如果有的话。
 send_keys 输入值，这个 alert\confirm 没有对话框就不能用了，不然会报错。
'''
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
#点击打开搜索设置
driver.find_element_by_name("tj_setting").click()
driver.find_element_by_id("SL_1").click()
#点击保存设置
driver.find_element_by_xpath("//div[@id='gxszButton']/input").click()
#获取网页上的警告信息
alert=driver.switch_to.alert()
#接收警告信息
alert.accept()
driver.quit()

#接受警告信息
alert = driver.switch_to_alert()
alert.accept()
#得到文本信息并打印
alert = driver.switch_to_alert()
print(alert.text())
