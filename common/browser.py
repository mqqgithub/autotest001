import time
import os
from selenium import webdriver


class Browser(object):
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

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        REPORT_PATH = os.path.join(os.path.dirname(os.getcwd()), "screen")
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        # screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        # return screenshot

    # 废弃
    def save_img(self, test_method): # 失败截图方法（必须要定义在class中）
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        img_path = root_dir + '/img'
        self.browser.get_screenshot_as_file('{}/{}.png'.format(img_path, test_method))

    # 关闭当前窗口
    def close(self):
        self.driver.close()

    # 关闭所哟窗口
    def quit(self):
        self.driver.quit()


# 这里试验了一下保存截图的方法，保存png截图到report目录下。
if __name__ == '__main__':
    b = Browser('chrome').get('https://zui.kjtpay.com/window/login#')
    b.save_screen_shot('login_page')
    time.sleep(3)
    b.save_img('123')
    time.sleep(3)
    b.quit()
