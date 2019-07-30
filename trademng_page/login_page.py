from selenium.webdriver.common.by import By
from common.page import Page

# 封装的百度首页

class LoginPage(Page):
    loc_username_input = (By.ID, 'userName')
    loc_password_btn = (By.ID, 'userPassword')
    loc_login_btn = (By.CLASS_NAME, 'login-btn')
    loc_showEnv_a = (By.ID, 'showEnv')
    loc_passwordError_p = (By.XPATH, '//*[@id="passwordError"]/p')

    def login(self, userName, userPassword):
        """搜索功能"""
        self.find_element(*self.loc_username_input).send_keys(userName)  #  输入用户名
        self.find_element(*self.loc_password_btn).send_keys(userPassword)  # 输入密码
        self.find_element(*self.loc_login_btn).click()

    def shouEnv(self):
        return self.find_element(*self.loc_showEnv_a).text
    def passwordError(self):
        return self.find_element(*self.loc_passwordError_p).text

if __name__=='__main__':
    p = LoginPage(browser_type='chrome').get('https://zui.kjtpay.com/window/login#')
    p.login("maqingqing", "kjt@1231")
    p.quit()
