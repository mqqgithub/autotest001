from seleniumTest.webdriverTest import openbrowser
import time

class findcss():

    b = openbrowser.openChrome()
    b.get("https://www.baidu.com")

if __name__=="__main__":
    bro = findcss().b
    '''css:属性定位
    1.css可以通过元素的id、class、标签这三个常规属性直接定位到
    2.如下是百度输入框的的html代码：
<input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd"/>
    3.css用#号表示id属性,如：#kw
    4.css用.表示class属性，如：.s_ipt'''
    bro.find_element_by_css_selector("#kw").send_keys("java")
    bro.find_element_by_css_selector(".s_ipt").send_keys("c++")