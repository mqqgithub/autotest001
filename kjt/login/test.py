from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
x = driver.find_element_by_xpath("//div/a[contains(text(), 新闻)]").text
print(x)
name = driver.find_element_by_css_selector("#kw")
id = driver.find_element_by_css_selector("#su")
elements = (name, id)
#elements[0].send_keys("java")
#elements[1].click()
print(1)


