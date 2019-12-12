from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.driver_type import DriverType


# 封装的百度首页
class LoginPage(BasePage):

    loc_username_input = (By.ID, 'userName')
    loc_password_btn = (By.ID, 'userPassword')
    loc_login_btn = (By.CLASS_NAME, 'login-btn')
    loc_showEnv_a = (By.ID, 'showEnv')
    loc_passwordError_p = (By.XPATH, '//*[@id="passwordError"]/p')

    # 登录功能
    def login(self, user_name, user_password):
        """搜索功能"""
        # self.find_element(*self.loc_username_input).send_keys(user_name)  # 输入用户名
        self.input_text(self.loc_username_input, user_name, 'user_name')
        # self.find_element(*self.loc_password_btn).send_keys(user_password)  # 输入密码
        self.input_text(self.loc_password_btn, user_password, 'user_password')
        # self.find_element(*self.loc_login_btn).click()
        self.click_element(self.loc_login_btn, 'login_btn')

    # 登录校验提示
    def shouEnv(self):
        return self.get_text(self.loc_showEnv_a, '提示')

    # 登录失败提示
    def passwordError(self):
        return self.get_text(self.loc_passwordError_p).text


if __name__ == '__main__':
    dr = DriverType("chrome").get("https://zui.kjtpay.com/window/index#")
    #page = BasePage(dr)
    p = LoginPage(dr)
    p.login("maqingqing", "kjt@1233")
    p.quit()
