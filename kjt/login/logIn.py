'''

'''
from selenium import webdriver
from kjt.login import openBro

class loginc():

    def login(self, driver, username, password):
        driver.get("https://zui.kjtpay.com/window/login#")
        driver.implicitly_wait(10)
        driver.maximize_window()
        userName = driver.find_element_by_id("userName")
        userPassword = driver.find_element_by_id("userPassword")
        login_btn = driver.find_element_by_class_name("login-btn")
        #tips = driver.find_element_by_class_name("tips")
        #logoutSpan = driver.find_element_by_id("logoutSpan")
        elements = (userName, userPassword, login_btn)
        elements[0].send_keys(username)
        elements[1].send_keys(password)
        elements[2].click()
    def login_re(self, driver, username, password):
        self.login(driver, username, password)
        logoutSpan = driver.find_element_by_id("logoutSpan")
        return logoutSpan
    def loginerror(self, driver, username, password):
        self.login(driver, username, password)
        tips = driver.find_element_by_class_name("tips")
        return tips


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
    loginc().login(driver, "maqingqing", "kjt@1231")
    #login().logout(driver)
    #driver.close()