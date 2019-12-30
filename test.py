from selenium import webdriver
from selenium.webdriver.common.by import By
import time
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
try:
    dr.find_element(By.ID, "kw").send_keys("12")
    time.sleep(5)
except Exception as e:
    dr.close()
