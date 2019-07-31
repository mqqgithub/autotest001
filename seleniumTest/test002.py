#元素定位的方法

from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_name("wd").send_keys("python")
driver.find_element_by_tag_name("input").send_keys("python")
driver.find_element_by_class_name("s_ipt").send_keys("python")

driver.find_element_by_link_text("新闻").click()
driver.find_element_by_partial_link_text("新闻").click()

driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
driver.find_element_by_xpath("//*[@id='kw]").send_keys("python")
driver.find_element_by_xpath("//div[@id='u1']/a[0]").send_keys("1")
driver.find_element_by_xpath("//div[@id='hd' or @name=q']").send_keys("2")
driver.find_element_by_xpath("//input[contains(@id,'kw')").send_keys("python")
driver.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
driver.find_element_by_xpath("//*[contains(.'新闻')]").click()#当标签里面含有其他标签+文字时

