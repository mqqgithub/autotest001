#鼠标事件ActionsChains
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#定位到要右击的元素
right = driver.find_element_by_xpath("xx")

#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right).perform()

double = driver.find_element_by_xpath("xx")
#对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(double).perform()

#拖放
#定位元素的原位置
element = driver.find_element_by_name("xxx")
#定位元素要移动到的目标位置
target = driver.find_element_by_name("xxx")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()

#移动到元素上
#定位到鼠标移动到上面的元素
above = driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(above).perform()

#按下左键不放
#定位到鼠标按下左键的元素
left=driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标左键按下的操作
ActionChains(driver).click_and_hold(left).perform()