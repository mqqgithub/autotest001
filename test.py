from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
chrome_driver_path = "C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://zui.kjtpay.com/window/index#')
driver.maximize_window()
driver.find_element_by_id('userName').send_keys('maqingqing')
driver.find_element_by_id('userPassword').send_keys('kjt@1233')
driver.find_element_by_class_name('login-btn').click()
time.sleep(3)
driver.find_element_by_class_name('showMore').click()
driver.find_element_by_xpath('//*[@id="topMenu"]/li[3]/a').click()
time.sleep(3)
#driver.find_element_by_xpath("//a[contains(.,'查询管理')]").click()
driver.find_element_by_xpath('//*[@id="848402AF91CD068AE0530A07FF0A5102"]/a').click()
driver.find_element_by_xpath('//*[@id="848402AF9224068AE0530A07FF0A5102"]/a').click()
time.sleep(2)
f1 = driver.find_element_by_xpath("//iframe[contains(@src,'trademng/unionQuery/query')]")
driver.switch_to.frame(f1)
time.sleep(3)
select = driver.find_element_by_id('defineId')

Select(select).select_by_visible_text("全部")
try:
    js1 = "document.getElementById('startTime').removeAttribute('readonly')"
    driver.execute_script(js1)
    # driver.find_element_by_xpath('//*[@id="startTime"]').clear()
    driver.find_element_by_id('startTime').clear()
    driver.find_element_by_xpath('//*[@id="startTime"]').send_keys('2019-12-31 23:08:52')
    js2 = "document.getElementById('endTime').removeAttribute('readonly')"
    driver.execute_script(js2)
    driver.find_element_by_xpath('//*[@id="endTime"]').clear()
    driver.execute_script("document.getElementById('endTime').value='2020-01-06 15:08:52'")
    # driver.find_element_by_xpath('//*[@id="endTime"]').send_keys('2020-01-06 15:08:52')
    driver.quit()
    print('2222222222222')
except:

    time.sleep(5)
    driver.quit()
    print('123123')