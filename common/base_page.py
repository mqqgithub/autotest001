# https://blog.csdn.net/qq_38741986/article/details/93237911
# https://testerhome.com/topics/19900
#
from common.driver_type import DriverType


# 创建基础类
class BasePage(object):
    # 初始化
    def __init__(self, driver):
        self.base_url = 'https://zui.kjtpay.com/window/login#'
        self.driver = driver
        self.timeout = 30

    # 打开页面
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        # self.driver.switch_to.frame('login_frame')  #切换到登录窗口的iframe

    def open(self):
        self._open()

    # 定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)


if __name__ == '__main__':
    dr = DriverType("chrome").get()
    d = BasePage(dr)
    d.open()