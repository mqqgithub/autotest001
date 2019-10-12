'''
iframe  frame  对象定位
在 web 应用中经常会出现 frame 嵌套的应用，假设页面上有 A、B 两个 frame，其中 B 在 A 内，那么
定位 B 中的内容则需要先到 A，然后再到 B。
switch_to_frame 方法可以把当前定位的主体切换了 frame 里。怎么理解这句话呢？我们可以从 frame
的实质去理解。frame 中实际上是嵌入了另一个页面，而 webdriver 每次只能在一个页面识别，因此才需要
用 switch_to.frame 方法去获取 frame 中嵌入的页面，对那个页面里的元素进行定位。
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

