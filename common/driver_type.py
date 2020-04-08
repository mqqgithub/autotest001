from selenium import webdriver


class DriverType(object):

    chrome_driver_path = "C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    browser = 'chrome'
    URL = {"统一登录": "https://zui.kjtpay.com/window/index#",
           "百度": "https://www.baidu.com"}

    def __init__(self, browser_type=browser):
        self._type = browser_type.lower()
        if self._type == "firefox":
            self.driver = webdriver.Firefox()
        if self._type == "chrome":
            self.driver = webdriver.Chrome(DriverType.chrome_driver_path)
        if self._type == "ie":
            self.driver = webdriver.Ie()

    '''    def get_url(self, url="统一登录"):
        if url == "统一登录":
            self.driver.get(self.URL["统一登录"])
            return self.driver
        if url == "百度":
            self.driver.get(self.URL["百度"])
            return self.driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)'''
    def get_url(self):
        self.driver.get(self.URL["统一登录"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver


if __name__ == "__main__":
    driver = DriverType().get_url(url="统一登录")
    driver.quit()