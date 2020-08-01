# 定位一组元素   find_elements_by_xx

from selenium import webdriver
from selenium.webdriver.common.by import By
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

'''
    find_element()：
    仅查找返回页面符合条件的第一个元素
    如果定位不到元素会报错
    find_elements()：
    是查找多个元素并且返回一个列表
    如果定位不到元素不会报错，返回一个空列表
'''
driver.find_elements(By.ID, "su")
driver.find_elements(By.NAME, "")
driver.find_elements(By.TAG_NAME, "")
driver.find_elements("link text", "")
driver.find_elements("partial link text", "")
driver.find_elements("class name", "")
driver.find_elements("xpath", "")
driver.find_elements("css selector", "")