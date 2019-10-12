# 定位一组元素   find_elements_by_xx

from selenium import webdriver
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
# 然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
for input1 in inputs:
    if input1.get_attribute('type') == 'checkbox':
        input1.click()
driver.quit()

#find_element()
driver.find_element("id", "su")
driver.find_element("name", "")
driver.find_element("tag name", "")
driver.find_element("link text", "")
driver.find_element("partial link text", "")
driver.find_element("class name", "")
driver.find_element("xpath", "")
driver.find_element("css selector", "")