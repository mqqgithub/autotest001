import os
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
print(os.getcwd())
print(os.path.dirname(os.getcwd()))
print(os.path.join(os.path.dirname(os.getcwd()), "screen"))

class Browser(object):

    def __init__(self, browse_type="chrome"):
        if browse_type == "chrome":
            self.browser = webdriver.Chrome()

    def get(self, url):
        self.driver = self.browser
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

class Page(Browser):

    def __init__(self, browse_type="chrome"):
        Browser.__init__(self, browse_type=browse_type)

    def current_window(self):
        return self.driver.current_window_handle

    def current_url(self):
        return self.driver.current_url

    def wait_time(self):
        time.sleep(2)

    def js(self, js, *args):
        self.driver.execute_script(js, *args)

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def switch_to_frame(self, param):
        self.driver.switch.to_frame(param)

    def back_from_frame(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, partial_url, partial_title):
        all_windows = self.driver.window_handles

        if len(all_windows) == 1:
            print(1)

        elif len(all_windows) == 2:
            other_window = all_windows[1- all_windows.index(self.current_window())]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break


if __name__ == "__main__":
    p = Page('chrome').get('https://www.baidu.com')
    print('122')