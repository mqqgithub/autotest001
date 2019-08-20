from selenium import  webdriver

d = webdriver.Chrome()
d.get("https://www.baidu.com")
d.maximize_window()
d.find_element_by_xpath("//input[contains(@id,'kw')]").send_keys("python")