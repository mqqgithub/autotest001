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
        logIn.login().login(self.driver, "maqingqing", "kjt@1231")


if __name__=="__main__":
    unittest.main(verbosity=2)


