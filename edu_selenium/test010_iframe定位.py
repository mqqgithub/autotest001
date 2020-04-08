'''
iframe  frame  对象定位
在 web 应用中经常会出现 frame 嵌套的应用，假设页面上有 A、B 两个 frame，其中 B 在 A 内，那么
定位 B 中的内容则需要先到 A，然后再到 B。
switch_to_frame 方法可以把当前定位的主体切换了 frame 里。怎么理解这句话呢？我们可以从 frame
的实质去理解。frame 中实际上是嵌入了另一个页面，而 webdriver 每次只能在一个页面识别，因此才需要
用 switch_to.frame（） 方法去获取 frame 中嵌入的页面，对那个页面里的元素进行定位。
'''


from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
# 先找到到 ifrome1（id = f1）
driver.switch_to.frame("f1")
# 再找到其下面的 ifrome2(id =f2)
driver.switch_to.frame("f2")
# 下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
# driver.switch_to.frame(reference)
# 从子frame切回到父frame
driver.switch_to.parent_frame()
# 切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档
driver.switch_to.default_content()
time.sleep(3)
driver.quit()

'''
def test_57o4(self):
        """expected_conditions模块下的frame_to_be_available_and_switch_to_it()"""
        # frame_to_be_available_and_switch_to_it() 判断该frame是否可以switch进去
        # 如果直接传入定位方式id，可以的话就返回True并switch进去，否则返回False
        # 也可传入locator元组或WebElement，可以的话就返回True并switch进去，否则报错，找不到定位

        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://mail.qq.com/")
        print('0', time.ctime())
        # <iframe id="login_frame" name="login_frame" height="100%" scrolling="no" width="100%" frameborder="0" src="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&amp;appid=522005705&amp;daid=4&amp;s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&amp;style=25&amp;low_login=1&amp;proxy_url=https://mail.qq.com/proxy.html&amp;need_qr=0&amp;hide_border=1&amp;border_radius=0&amp;self_regurl=http://zc.qq.com/chs/index.html?type=1&amp;app_id=11005?t=regist&amp;pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&amp;css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input24e6b9.css"></iframe>

        # 直接传入定位方式id
        # print(EC.frame_to_be_available_and_switch_to_it('login_frame')(self.driver))        # 正确的 返回True并switch进去
        # print(EC.frame_to_be_available_and_switch_to_it('login_frame123')(self.driver))     # 错误的 返回False

        # 传入locator元组
        # print(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[frameborder="0"][width="100%"]'))(self.driver))       # 正确的 返回True并switch进去
        # print(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[frameborder="10"]'))(self.driver))    # 报错 Message: no such element

        # 传入WebElement
        abcd = self.driver.find_element(By.XPATH, '//iframe[@height="100%" and @scrolling="no"]')       # 正确的 返回True并switch进去
        # abcd = self.driver.find_element(By.XPATH, '//iframe[@height="1000%" and @scrolling="no123"]')       # 报错 Message: no such element
        print(EC.frame_to_be_available_and_switch_to_it(abcd)(self.driver))

        self.driver.find_element_by_id("switcher_plogin").click()
        self.driver.find_element_by_id("u").clear()
        self.driver.find_element_by_id("u").send_keys('987654')
        self.driver.switch_to.default_content()
        print('1', time.ctime())

        time.sleep(1)
        self.driver.quit(
# ###############################################################
# 原文链接：https://blog.csdn.net/zyooooxie/article/details/84033754
'''