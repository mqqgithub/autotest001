# 打印信息
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

print(driver.page_source)
