from selenium import  webdriver

d = webdriver.Chrome()
d.get("https://www.baidu.com")
d.maximize_window()
#d.find_element_by_xpath("//*[contains(.'新闻')]").click()
text = d.find_element_by_xpath("//*[contains(text(),'新闻')]").text
print(text)
d.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
#d.find_element_by_xpath('//*[text()="新闻"]').click()