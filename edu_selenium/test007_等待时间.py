# 等待时间 https://www.jianshu.com/p/01940c63160c

# 导入 WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

'''显示等待WebDriverWait()方法使用'''
# element = WebDriverWait(driver, 10).until(lambda dr: driver.find_element_by_id("kw"))
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'kw')))
element = WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element_by_id("kw")))
element.send_keys("selenium")

'''添加智能等待,隐式等待，遇到js问题可能就会一直等待'''
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()

'''添加固定休眠时间'''
time.sleep(5)
driver.quit()

'''
title_is:判断当前页面的title是否完全等于（==）预期字符串，返回是布尔值
title_contains 判断当前页面的title是否包含预期字符串，返回布尔值
presence_of_element_located:判断某个元素是否被加到了dom树里，并不代表该元素一定可见
visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
visibility_of :跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
presence_of_all_elements_located : 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
text_to_be_present_in_element : 判断某个元素中的text是否 包含 了预期的字符串
text_to_be_present_in_element_value:判断某个元素中的value属性是否 包含 了预期的字符串
frame_to_be_available_and_switch_to_it : 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
invisibility_of_element_located : 判断某个元素中是否不存在于dom树或不可见
element_to_be_clickable : 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
staleness_of :等某个元素从dom树中移除，注意，这个方法也是返回True或False
element_to_be_selected:判断某个元素是否被选中了,一般用在下拉列表
＞* element_selection_state_to_be:判断某个元素的选中状态是否符合预期
element_located_selection_state_to_be:跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
alert_is_present : 判断页面上是否存在alert
'''

'''
selenium的显示等待
原理：显示等待，就是明确的要等到某个元素的出现或者是某个元素的可点击等条件，等不到，就一直等，除非在规定的时间之内都没找到，那么久跳出Exception
(简而言之，就是直到元素出现才去操作，如果超时则报异常)，针对某个特定的元素

driver = webdriver.Chrome()
driver.get('http://www.baidu')
 
element = WebDriverWait(driver,5,0.5).util(
                  EC.presence_of_element_located((By.ID,'kw'))
                    )  
element.send_keys('hello')
driver.quit()
-------------
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
driver:浏览器驱动
timeout:最长超过时间，默认以秒为单位
poll_frequency:监测的时间间隔，默认为0.5秒
ignored_exceptions:超时后的异常信息，默认情况下抛NoSuchElementException异常
WebDriverWait一般有until和until_not方法配合使用
until(method,message)
until_not(method ,message)
------------------
selenium的隐式等待
原理：隐式等待，就是在创建driver时，为浏览器对象创建一个等待时间，这个方法是得不到某个元素就等待一段时间，直到拿到某个元素位置。
注意：在使用隐式等待的时候，实际上浏览器会在你自己设定的时间内部断的刷新页面去寻找我们需要的元素
driver.implicity_wait(10),全局的等待时间，针对页面所有的元素，只要没有找到，就等待这么长时间
缺点：
当页面某些js无法加载，但是想找的元素已经出来了，它还是会继续等待，直到页面加载完成（浏览器标签左上角圈圈不再转），
才会执行下一句。某些情况下会影响脚本执行速度。




'''