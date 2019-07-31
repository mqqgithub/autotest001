#浏览器的相关操作
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.set_window_size(1000, 800)
driver.get("https://www.google.com")
driver.back()
driver.forward()
driver.quit()#当前浏览器
driver.close()#多个浏览器期
