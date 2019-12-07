from selenium import webdriver


class DriverType(object):

    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type == "firefox":
            self.browser = webdriver.Firefox()
        if self._type == "chrome":
            self.browser = webdriver.Chrome("C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        if self._type == "ie":
            self.browser = webdriver.Ie()
        else:
            self.driver = None

    def get(self, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self.driver
