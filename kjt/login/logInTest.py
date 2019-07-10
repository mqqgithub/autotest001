'''

'''
import unittest
from kjt.login import logIn
from kjt.login import openBro
class logintest(unittest.TestCase):
    def setUp(self):
        print("start")
        self.driver = openBro.openbroswer()
    def tearDown(self):
        print("ending")
        self.driver.close()
    def test_login_001(self):
        self.logoutSpan = logIn.loginc().login_re(self.driver, "maqingqing", "kjt@1231")
        self.assertEqual(self.logoutSpan.text, u"注销")
    def test_login_002(self):
        self.logoutSpan = logIn.loginc().login(self.driver, "maqingqing", "kjt@1231")
        self.login_btn = logIn.loginc().logout(self.driver)
        self.assertEqual(self.login_btn.get_attribute("value"), u"登录")
    def test_login_003(self):
        self.tips = logIn.loginc().loginerror(self.driver, "", "kjt@1231")
        self.assertEqual(self.tips.text, u"请输入正确的用户名称")
    def test_login_004(self):
        self.tips = logIn.loginc().loginerror(self.driver, "maqingqing", "kjt")
        self.assertEqual(self.tips.text, u"请输入正确的用户名称")
if __name__=="__main__":
    unittest.main(verbosity=2)


