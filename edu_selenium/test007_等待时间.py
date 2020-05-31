# 等待时间 https://www.jianshu.com/p/01940c63160c

# 导入 WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

'''显示等待WebDriverWait()方法使用'''
element = WebDriverWait(driver, 10).until(lambda dr: driver.find_element_by_id("kw").is_displayed())
element.send_keys("selenium")

'''添加智能等待,隐式等待，遇到js问题可能就会一直等待'''
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()

'''添加固定休眠时间'''
time.sleep(5)
driver.quit()

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





'''