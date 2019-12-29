import time
import unittest
from trademng_page.login_page import LoginPage
from test_utils.log import TestLog
# from BeautifulReport import BeautifulReport

log = TestLog().get_log()

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.p = LoginPage(browser_type='chrome').get('https://zui.kjtpay.com/window/login#')

    def tearDown(self):
        time.sleep(2)
        self.p.quit()

    def test_login_001(self):
        """登录测试：登录成功(报告描述中展示, 必须在首行)"""
        log.info('登录测试：登录成功，记录在日志中')
        print('登录测试：登录成功,详情中展示')
        print("test start")
        self.p.login("maqingqing", "kjt@1233")
        self.assertEqual(self.p.shouEnv(), u"马庆庆", "登录失败")
        print("test ending")

    # 不执行该用例
    @BeautifulReport.stop
    def test_login_002(self):
        log.info('登录测试：登录用户名为空，密码为空')
        self.p.login("", "")
        self.assertEqual(self.p.passwordError(), u"请输入正确的用户名称")


    def test_login_003(self):
        log.info('登录测试：登录用户名为空，密码不为空')
        self.p.login("", "123")
        self.assertEqual(self.p.passwordError(), u"请输入正确的用户名称")


    def test_login_004(self):
        log.info("登录测试：登录用户名bu 为空，密码为空")
        self.p.login("maqingqing", "")
        self.assertEqual(self.p.passwordError(), u"请输入正确的密码！")

if __name__ == "__main__":
    unittest.main(verbosity=2)
