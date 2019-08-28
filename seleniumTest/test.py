from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)
driver.implicitly_wait(20)
# 鼠标移动到"设置"按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
#分两步：先定位下拉框，再点击选项
s = driver.find_element_by_xpath("//*[@id='nr']")
time.sleep(3)
print()
Select(s).select_by_index(0)
time.sleep(2)
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='20']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='nr']/option[2]").click()

