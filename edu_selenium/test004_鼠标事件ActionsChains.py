# 鼠标事件ActionsChains
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


'''定位到要右击的元素'''
right = driver.find_element_by_xpath("xx")

'''对定位到的元素执行鼠标右键操作'''
ActionChains(driver).context_click(right).perform()

'''双击'''
double = driver.find_element_by_xpath("xx")
# 对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(double).perform()

'''拖放'''
# 定位元素的原位置
element = driver.find_element_by_name("xxx")
# 定位元素要移动到的目标位置
target = driver.find_element_by_name("xxx")
# 执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()

'''鼠标移动到元素上'''
# 定位到鼠标移动到上面的元素
above = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(above).perform()

'''按下左键不放 '''
# 定位到鼠标按下左键的元素
left = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标左键按下的操作
ActionChains(driver).click_and_hold(left).perform()
# 某个元素上松开鼠标左键,接收elementObj
ActionChains(driver).release()

'''链式操作'''
fl = driver.find_element_by_css_selector('#a')  # 获取鼠标要悬浮的元素
dis1 = driver.find_element_by_css_selector('#dis1')  # 获取要点击的按钮
ActionChains(driver).move_to_element(fl).click(dis1).perform() # 链式编程，可以一直点下去

'''移动到坐标上'''
# 鼠标移动到制定的坐标上，参数接受x，y
ActionChains(driver).move_by_offset(e['x'], e['y'])


# 将一个source元素 拖动到针对source坐上角坐在的x y处 可存在负宽度的情况和负高度的情况
ActionChains(driver).drag_and_drop_by_offset(source, x, y)
# 这种也是拖拽的一种方式，都是以源元素的左上角为基准，移动坐标
ActionChains(driver).click_and_hold(dom).move_by_offset(169, 188).release().perform()