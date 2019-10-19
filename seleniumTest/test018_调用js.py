# 调用 JavaScript

from selenium import webdriver
import time,os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('js.html')
driver.get(file_path)
#######通过 JS 隐藏选中的元素##########第一种方法：
#隐藏文字信息
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)
#隐藏按钮：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()', button)
time.sleep(5)
driver.quit()

# execute_script(script, *args)
# 在当前窗口/框架 同步执行 javaScript
# script：JavaScript 的执行。
# *args：适用任何 JavaScript 脚本。
