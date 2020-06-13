from selenium import webdriver


class DriverType(object):

    chrome_driver_path = "C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    browser = 'chrome'
    host = ["http://127.0.0.1:4444/wd/hub", "http://127.0.0.1:5555/wd/hub", "http://127.0.0.1:6666/wd/hub"]
    URL = {"统一登录": "https://zui.kjtpay.com/window/index#",
           "百度": "https://www.baidu.com"}

    '''
    # 远程分布式执行  host执行为主机地址，grid自动分发
    def __init__(self, browser_type=browser):
        self.capabilities = {
            'platform': 'ANY',
            'browserName': browser_type,
            'version': '',
            'javascriptEnabled': True
        }
        self._type = browser_type.lower()
        if self._type == "chrome":
            self.dr = webdriver.remote(command_executor=DriverType.host[0], desired_capabilities=self.capabilities)
    '''

    # 本地线性批量执行
    def __init__(self, browser_type=browser):
        self._type = browser_type.lower()
        if self._type == "firefox":
            self.driver = webdriver.Firefox()
        if self._type == "chrome":
            self.driver = webdriver.Chrome()
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
    driver = DriverType().get_url()
    driver.quit()