from selenium.webdriver.common.by import By
from common.base_page import BasePage


# 封装的百度首页
class LoginPage(BasePage):

    loc_username_input = (By.ID, 'userName')
    loc_password_btn = (By.ID, 'userPassword')
    loc_login_btn = (By.CLASS_NAME, 'login-btn')
    loc_showEnv_a = (By.ID, 'showEnv')
    loc_passwordError_p = (By.XPATH, '//*[@id="passwordError"]/p')
    loc_more_a = (By.CLASS_NAME, "showMore")
    loc_system_a = (By.XPATH, "//a[@data-sys-name='trademng']")

    # 登录功能
    def login(self, user_name, user_password):
        """搜索功能"""
        # self.find_element(*self.loc_username_input).send_keys(user_name)  # 输入用户名
        self.input_text(self.loc_username_input, user_name, 'user_name')
        # self.find_element(*self.loc_password_btn).send_keys(user_password)  # 输入密码
        self.input_text(self.loc_password_btn, user_password, 'user_password')
        # self.find_element(*self.loc_login_btn).click()
        self.click_element(self.loc_login_btn, 'login_btn')

    # 登录成功，跳转页面显示用户名控件
    def shouEnv(self):
        return self.get_text(self.loc_showEnv_a, '登录成功显示用户名提示')

    # 登录失败页面提示控件
    def passwordError(self):
        return self.get_text(self.loc_passwordError_p, '登录失败页面提示错误信息')

    #  登录并定位到对应的测试系统
    def login_to_system(self):
        self.login("maqingqing", "kjt@1233")
        self.click_element(self.loc_more_a, "点更多按钮方便选择系统")
        self.click_element(self.loc_system_a, "点击选择系统")


if __name__ == '__main__':
    p = LoginPage()
    #p.login("maqingqing", "kjt@1233")
    p.login_to_system()
    p.quit()
