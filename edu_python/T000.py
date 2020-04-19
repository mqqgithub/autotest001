import unittest
from selenium import webdriver
import time

chrome_capabilities = {
            'platform': 'ANY',
            'browserName': 'chrome',
            'version': '',
            'javascriptEnabled': True
        }


class Test(unittest.TestCase):
    def setUp(self):
        print("test start...>")
        self.x = 5
        self.y = 2
        # self.host = "http://192.168.2.128:4444/wd/hub"
        self.host = "http://192.168.170.78:4444/wd/hub"
        self.dr = webdriver.Remote(command_executor=self.host, desired_capabilities=chrome_capabilities)
        time.sleep(3)

    def tearDown(self):
        print("test over...>")
        self.dr.quit()

    def test_01(self):
        z = self.x / self.y
        self.assertEqual(z, 2.5, msg="除以")

    def test_02(self):
        z = self.x // self.y
        self.assertEqual(z, 2, msg="商")

    def test_03(self):
        z = self.x % self.y
        self.assertEqual(z, 1, msg="余数")

    def test_04(self):
        z = self.x ** self.y
        self.assertEqual(z, 25, msg="乘方")

    def test_05(self):
        self.dr.get("https://www.baidu.com")

    def test_06(self):
        self.dr.get("https://www.baidu.com")


if __name__ == "__main__":
    unittest.main()




