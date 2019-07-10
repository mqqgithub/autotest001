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
        self.logoutSpan = logIn.login().login(self.driver, "maqingqing", "kjt@1231")
        self.assertEqual(self.logoutSpan.text, u"注销")
    def test_login_002(self):
        self.logoutSpan = logIn.login().login(self.driver, "maqingqing", "kjt@1231")
        self.login_btn = logIn.login().logout(self.driver)
        self.assertEqual(self.login_btn.get_attribute("value"), u"登录")

if __name__=="__main__":
    unittest.main(verbosity=2)


