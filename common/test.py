from selenium.webdriver.common.by import By
from common.driver_type import DriverType
from common.base_page import BasePage
loc_username_input = (By.ID, 'userName')
loc_password_btn = (By.ID, 'userPassword')
loc_login_btn = (By.CLASS_NAME, 'login-btn')

dr = DriverType("chrome").get("https://zui.kjtpay.com/window/index#")
page = BasePage(dr)
page.input_text(loc_username_input, 'maqingqing', 'input username')
page.input_text(loc_password_btn, 'kjt@1233', 'input password')
page.click_element(loc_login_btn, 'click submit')
