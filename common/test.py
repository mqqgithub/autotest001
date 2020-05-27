from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.find_element_by_xpath('//*[]')