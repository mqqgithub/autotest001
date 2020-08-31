from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
d = webdriver.Chrome()
d.get("https://www.baidu.com")
# d.find_element_by_xpath("//*[match(text(), 'hao123']").click()
# d.find_element(*(By.ID, "kw")).send_keys("123")
cook = d.get_cookies()
time.sleep(3)
print(cook)
d.quit()