from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest, os


class test_test(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get("https://www.baidu.com")

    def test(self):
        kw = WebDriverWait(self.dr, 10).until(EC.visibility_of_element_located((By.ID, 'kw')))
        kw.send_keys('selenium')
        su = WebDriverWait(self.dr, 10).until(EC.visibility_of_element_located((By.ID, 'su')))
        su.click()

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    t
