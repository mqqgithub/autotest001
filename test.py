from selenium.webdriver.common.by import By
from common.base_page import BasePage
import time

class Test(BasePage):
    def __init__(self):
        self.loc_username_input = (By.ID, 'userName')
    def test1(self):
        self.input_text(self.loc_username_input, "123")
        time.sleep(5)


if __name__=="__main__":
    p=Test()
    p.test1()