from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fvod.kuaibo.com%2F%3Fly%3Ddefault")
# 登录系统
driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()
sleep(2)
# 获取所有分页的数量，并打印
total_pages = len(driver.find_element_by_tag_name("select").find_elements_by_tag_name("option"))
print("total page is %s" %(total_pages))
sleep(3)
# 再次获取所分页，并执行循环翻页操作
pages = driver.find_element_by_tag_name("select").find_elements_by_tag_name("option")
for page in pages:
    page.click()
    sleep(2)
sleep(3)
'''len()方法在定位一组对象有时已经用过，用于获取对象的个数。
这里同样用到了二次定位，只是第二次定位用的是 find_elements 方法，获取的是一组元素。通过上
面的脚本可以看到，我们第一次获取到一组元素后，打印了所有分页的个数。第二次获取所有分页后， 通
过 for 循环来翻阅每一页，每翻一页休眠 2 秒，当然，我们也可以在翻页后对列表的文件做更多操作'''