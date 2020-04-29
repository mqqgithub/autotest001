# 下拉框处理
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)
driver.implicitly_wait(20)
# 鼠标移动到"设置"按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
# --------------------------一定要设置等待时间
#time.sleep(2)
#driver.find_element_by_xpath("//*[@id='nr']/option[2]").click()
# --------------------------
#time.sleep(2)
#driver.find_element_by_id("nr").find_element_by_xpath("//option[1]").click()
# --------------------------
#time.sleep(2)
s = driver.find_element_by_id("nr")
'''通过索引'''
#Select(s).select_by_index(0)
''''''
#Select(s).select_by_value("20")
# --------------------------
time.sleep(2)
Select(s).select_by_visible_text("每页显示50条")
print("over")
