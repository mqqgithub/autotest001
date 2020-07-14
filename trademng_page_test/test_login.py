import time
# from selenium import webdriver
import unittest
from BeautifulReport import BeautifulReport

from common.driver_type import DriverType
from trademng_page.login_page import LoginPage
from test_utils.log import Log

log = Log()


class TestLogin(unittest.TestCase):

    def setUp(self):

        # 初始化浏览器
        self.driver = DriverType().get_url()
        # 创建登录页面对象，并初始化基类
        self.p = LoginPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login_001(self):
        """登录测试：登录成功(报告描述中展示, 必须在首行)"""
        log.info('登录测试：登录成功，记录在日志中')
        print('登录测试：登录成功,详情中展示')
        print("test start")

        self.p.login("maqingqing", "kjt@2121")
        self.assertEqual(self.p.shouEnv(), u"马庆庆", "登录失败")

        print("test ending")

    # 不执行该用例
    @BeautifulReport.stop
    def test_login_002(self):
        """ 登录测试：登录用户名为空，密码为空"""
        log.info('登录测试：登录用户名为空，密码为空')

        self.p.login("", "")
        self.assertEqual(self.p.passwordError(), u"请输入正确的用户名称")

    def test_login_003(self):
        """登录测试：登录用户名为空，密码不为空"""
        log.info('登录测试：登录用户名为空，密码不为空')

        self.p.login("", "123")
        self.assertEqual(self.p.passwordError(), u"请输入正确的用户名称")

    def test_login_004(self):
        """登录测试：登录用户名bu 为空，密码为空"""
        log.info("登录测试：登录用户名bu 为空，密码为空")

        self.p.login("maqingqing", "")
        self.assertEqual(self.p.passwordError(), u"请输入正确的密码")

    def test_login_005(self):
        """登录测试：登录用户名正确，密码正确"""
        log.info("登录测试：登录用户名正确，密码正确")

        self.p.login("maqingqing", "kjt@1212")


if __name__ == "__main__":
    unittest.main(verbosity=2)
