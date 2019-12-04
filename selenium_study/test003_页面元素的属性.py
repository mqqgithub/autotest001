from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

size = driver.find_element_by_id("su").size
print(size)

text = driver.find_element_by_id("su").text
print(text)

value = driver.find_element_by_id("su").get_attribute('value')
print(value)

#返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
type = driver.find_element_by_id("su").get_attribute('type')
print(type)

#返回元素的结果是否可见，返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)
