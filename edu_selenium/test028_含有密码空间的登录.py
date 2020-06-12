import time
from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('https://c1w.kjtpay.com/index.htm')
dr.find_element_by_xpath("//a[text()='个人会员']").click()
dr.find_element_by_id('username').send_keys('mqq_kjt001@163.com')
# js = "document.getElementById('passwordControl').value='kjt12345'"
# dr.execute_script(js)
dr.find_element_by_id('person_index_passwordkeyboardBtn').click()
dr.find_element_by_xpath("//li[text()='k']").click()
dr.find_element_by_xpath("//li[text()='j']").click()
dr.find_element_by_xpath("//li[text()='t']").click()
dr.find_element_by_xpath("//li[text()='1']").click()
dr.find_element_by_xpath("//li[text()='2']").click()
dr.find_element_by_xpath("//li[text()='3']").click()
dr.find_element_by_xpath("//li[text()='4']").click()
dr.find_element_by_xpath("//li[text()='5']").click()
dr.find_element_by_xpath("//span[text()='确定']").click()
dr.find_element_by_id('vercode').send_keys('Ed8r5')
# dr.find_element_by_id('kjt_personal_index_login').click()
# dr.find_element_by_id('kjt_personal_index_login').submit()   # 必须要是表单提交的方式
js = "document.getElementById('kjt_personal_index_login').click()"
dr.execute_script(js)
time.sleep(10)
dr.quit()
