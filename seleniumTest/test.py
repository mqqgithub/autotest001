from selenium import  webdriver

d = webdriver.Chrome()
d.get("https://www.baidu.com")
d.maximize_window()
d.find_element_by_css_selector("input[class^='s']").send_keys("python")
#d.find_element_by_css_selector("input[class~='bg']").click()
d.find_element_by_css_selector("#su").submit()