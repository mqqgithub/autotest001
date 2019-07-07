'''
浏览器相关的操作
'''


import time
from selenium import webdriver

class openbrowser():
    def openChrome(self):
        driver = webdriver.Chrome()
        return  driver
    def openFirefox(self):
        driver = webdriver.Firefox()
        return driver
    def openIe(self):
        driver = webdriver.Ie()
        return driver

if __name__=='__main__':
    browser = openbrowser().openChrome()
    browser.get('https://www.baidu.com')
    # 等待2秒
    time.sleep(2)
    #刷新页面
    browser.refresh()
    browser.find_element_by_id('kw').send_keys('BNA')
    browser.find_element_by_id('su').click()
    #返回上一页
    browser.back()
    #前一页面
    browser.forward()
    #设置窗口大小 ，手机测试可能用到
    browser.set_window_size(540, 960)
    #最大化页面
    browser.maximize_window()
    #截屏
    browser.get_screenshot_as_file('d:\\autotest001\\b1.png')
    #关闭浏览器
    '''
    #1.退出有两种方式，一种是close;另外一种是quit
    #2.close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口
    #3.quit用于结束进程，关闭所有的窗口
    #4.最后结束测试，要用quit。quit可以回收c盘的临时文件'''
    browser.close()

