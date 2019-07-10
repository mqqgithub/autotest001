from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
name = driver.find_element_by_css_selector("#kw").get_attribute("name")
print(name)
