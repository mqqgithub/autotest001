
# 层级定位
# 页面上有很多个属性基本相同的元素 ，现在需要具体定位到其中的一个。
# 由于属性基本相当，所以在定位的时候会有些麻烦，这时候就需要用到层级定位。
# 先定位父元素，然后再通过父元素定位子孙元素

from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
# 点击 Link1 链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
# 在父亲元件下找到 link 为 Action 的子元素
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Anotheraction')
# 鼠标移动到子元素上 ，perform()执行所有 ActionChains 中存储的行为
ActionChains(driver).move_to_element(menu).perform()
time.sleep(5)
driver.quit()
