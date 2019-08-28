import os
import time
import unittest
from trademng_page.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.p = LoginPage(browser_type='chrome').get('https://zui.kjtpay.com/window/login#')
    def tearDown(self):
        time.sleep(2)
        self.p.quit()
    def test_login_001(self):
        self.p.login("maqingqing", "kjt@1232")
        self.assertEqual(self.p.shouEnv(), u"马庆庆", "登录失败")
    def test_login_002(self):
        self.p.login("", "")
        self.assertEqual(self.p.passwordError(), u"请输入正确的用户名称")
    def test_login_003(self):
        self.p.login("", "123")
        self.assertEqual(self.p.passwordError(), u"请输入正确的用户名称")
    def test_login_004(self):
        self.p.login("maqingqing", "")
        self.assertEqual(self.p.passwordError(), u"请输入正确的密码")

if __name__=="__main__":
    unittest.main()