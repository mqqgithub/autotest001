from selenium import webdriver


class DriverType(object):

    chrome_driver_path = "C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    browser = 'chrome'
    URL = "https://zui.kjtpay.com/window/index#"

    def __init__(self, browser_type=browser):
        self._type = browser_type.lower()
        if self._type == "firefox":
            self.driver = webdriver.Firefox()
        if self._type == "chrome":
            self.driver = webdriver.Chrome(DriverType.chrome_driver_path)
        if self._type == "ie":
            self.driver = webdriver.Ie()

    def get_url(self, url=URL):

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)
        return self.driver


if __name__ == "__main__":
    driver = DriverType().get_url("https://www.baidu.com")
    driver.close()