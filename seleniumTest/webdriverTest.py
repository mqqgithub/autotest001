'''

'''



from selenium import webdriver

class openbrowser():
    def openChrome(self):
        driver = webdriver.Chrome()
        return  driver
    def openFirefox(self):
        driver = webdriver.Firefox()
        return driver
    def openIe(self):
        driver = webdriver.Ie()
        return driver

if __name__=='__main__':
    browser = openbrowser().openChrome()
    browser.get('https://www.baidu.com')
