from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("aa")
el = WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, "su")))
el.click()


