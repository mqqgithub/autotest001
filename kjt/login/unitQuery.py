'''

'''
from kjt.login import logIn
from kjt.login import openBro
class unintqueryc():

    def unintquery(self, ):
        #
        driver = openBro.openbroswer()
        #
        logIn.loginc().login(driver, "maqingqing", "kjt@1231")
        showMore = driver.find_element_by_class("showMore")
        showMore.click()
        #queryM = driver.find_element_by_xpath("///html/body/div[1]/aside/div/section/div/ul/li[1]/a/span[1]")
        #
        queryM = driver.find_element_by_xpath("//span[text()='查询管理']")
        #
        queryM = driver.find_element_by_xpath("//span[contains(text()='查询管理')]")
        queryM.click()



