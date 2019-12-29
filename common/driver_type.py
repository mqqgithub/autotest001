from selenium import webdriver


class DriverType(object):

    chromedriver_path = "C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"

    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type == "firefox":
            self.browser = webdriver.Firefox()
        if self._type == "chrome":
            self.browser = webdriver.Chrome(DriverType.chromedriver_path)
        if self._type == "ie":
            self.browser = webdriver.Ie()
        else:
            self.browser = None

    def get(self, url):
        self.driver = self.browser
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)
        return self.driver


if __name__ == "__main__":
    url = "https://zui.kjtpay.com/window/index#"
    driver = DriverType("chrome").get(url)