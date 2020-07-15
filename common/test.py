from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
ele = WebDriverWait(driver).until(EC.visibility_of_element_located())