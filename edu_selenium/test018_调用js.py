# 调用 JavaScript
# https://www.cnblogs.com/wangtingting920416/category/1405411.html
# https://www.cnblogs.com/cmnz/p/9099473.html
from selenium import webdriver
import time
import os
'''隐藏按钮
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('js.html')
driver.get(file_path)
#######通过 JS 隐藏选中的元素##########第一种方法：
#隐藏文字信息
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)
#隐藏按钮：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()', button)
time.sleep(5)
driver.quit()
'''
# 清空输入框文本
'''
driver = webdriver.Chrome()
driver.get("https://wwww.baidu.com")
loc = ("id", "kw")
input_text = driver.find_element(*loc)
input_text.send_keys("123")
time.sleep(3)
js = 'document.querySelector("#kw").value="";'
driver.execute_script(js)
input_text.send_keys("111111")
time.sleep(3)
driver.close()
'''
# web 界面的滑动
'''
from  selenium import webdriver
import time

d = webdriver.Firefox()
d.implicitly_wait(10)
d.maximize_window()
d.get(r'https://www.tmall.com/')
time.sleep(10)
# 用JS获取HTML元素焦点，滚动条就自动滑动到焦点所在位置
# .mui-mbar-tab.mui-mbar-tab-cart.mui-mbar-tab-cart-nologin>div:nth-child(2)
# 查找class属性值为"mui-mbar-tab mui-mbar-tab-cart mui-mbar-tab-cart-nologin"的元素下的第二个div元素
ele = d.find_element_by_css_selector('.mui-mbar-tab.mui-mbar-tab-cart.mui-mbar-tab-cart-nologin>div:nth-child(2)')
#print ele.text
# 获取一个焦点
js = "arguments[0].scrollIntoView();"   
# 获取ele元素所在的位置焦点，滚动条会自动的滑动到获取的焦点位置
d.execute_script(js,ele)   
'''
# js来拖动滚动条滚动到具体位置
'''
js_="window.scrollTo(400,700);"
driver.execute_script(js_)
'''
#  选择控件日期
'''
js="$('#SystemDate').val('2017-07-21');"    
driver.execute_script(js 
'''

# 移除只读属性
'''
js="document.getElementById('promote_start_date').removeAttribute('readonly')"
    driver.execute_script(js)
    driver.find_element_by_id('promote_start_date').clear() 
    # 填写促销日期（promote_start_date）为日期控件的id
    driver.find_element_by_id('promote_start_date').send_keys('1996-05-25') 
'''




# execute_script(script, *args)
# 在当前窗口/框架 同步执行 javaScript
# script：JavaScript 的执行。
# *args：适用任何 JavaScript 脚本。
'''
DOM 它是提供一个API给编程语言，比如Javascript
Javascript可以通过DOM直接访问和操作网页文档的内容，一开始，DOM是为方便Javascript操作设计的API。但其实发展到后来，他们是两个独立的个体。而且Javascript不是唯一可以使用DOM的编程语言，比如python也可以访问DOM。

http请求过程
浏览器输入的网址在通过DNS解析后得到服务器地址
浏览器向服务器发起http请求，经过TCP/IP三次握手确认链接后，服务器将需要的代码发回给浏览器。
浏览器接收到代码后进行解析，经过三大步骤：
DOM构造、布局以及绘制页面，最终展现为人人都能看懂的网页。
***************
BOM，browser object model，浏览器对象模型，这个对象就是对应着浏览器窗口window。
它提供了一些方法用于访问浏览器的功能，这些功能和网页内容无关。

'''