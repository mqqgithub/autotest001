# 浏览器多窗口处理
# 要想在多个窗口之间切换，首先要获得每一个窗口的唯一标识符号（句柄）。通过获得的句柄来区别
# 分不同的窗口，从而对不同窗口上的元素进行操作。

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
# 获得当前窗口
nowhandle = driver.current_window_handle
# 打开注册新窗口
driver.find_element_by_name("tj_reg").click()
# 获得所有窗口
allhandles = driver.window_handles
# 循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to.window(handle)
        print('now register window!')
# 切换到邮箱注册标签
driver.find_element_by_id("mailRegTab").click()
time.sleep(5)
driver.close()

# 回到原先的窗口
driver.switch_to.window(nowhandle)
driver.find_element_by_id("kw").send_keys(u"注册成功！")
time.sleep(3)
driver.quit()

'''法二：使用下表'''
h = driver.current_window_handle
allhandles = driver.window_handles
driver.switch_to.window(allhandles[1])
driver.switch_to.window(h)
