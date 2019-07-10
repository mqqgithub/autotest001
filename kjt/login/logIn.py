'''

'''
from selenium import webdriver
from kjt.login import openBro

class login():

    def login(self, driver, username, password):
        driver.get("https://zui.kjtpay.com/window/login#")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element_by_id("userName").send_keys(username)
        driver.find_element_by_id("userPassword").send_keys(password)
        driver.find_element_by_class_name("login-btn").click()
        logoutSpan = driver.find_element_by_id("logoutSpan")
        return logoutSpan
    def logout(self, driver):
        logoutSpan = driver.find_element_by_id("logoutSpan")
        logoutSpan.click()
        driver.find_element_by_class_name("layui-layer-btn0").click()
        login_btn = driver.find_element_by_class_name("login-btn")
        return login_btn
        #不是confirm、alert、prompt
        #driver.switch_to_alert().accept()
        #driver.switch_to_alert().dismiss()


if __name__=="__main__":
    #driver = webdriver.Chrome()
    driver = openBro.openbroswer()
    login().login(driver, "maqingqing", "kjt@1231")
    login().logout(driver)
    driver.close()