'''

'''
from kjt.login import logIn
from kjt.login import openBro
class unintqueryc():

    def unintquery(self, ):
        driver = openBro.openbroswer()
        logIn.loginc().login(driver, "maqingqing", "kjt@1231")
        showMore = driver.find_element_by_class("showMore")
        showMore.click()
        queryM = driver.find_element_by_xpath("//span[]")



