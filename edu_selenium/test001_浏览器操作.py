# 浏览器的相关操作
from selenium import webdriver

'''需要能找到驱动的位置，也可以在环境变量中'''
# driver = webdriver.Chrome("D:\\TOOLS\jenkins\\browser_driver\\chromedriver.exe")
# driver = webdriver.Chrome("C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
driver = webdriver.Chrome()
'''get 网址 '''
driver.get("https://www.baidu.com")
'''最大、最小、具体大小'''
driver.maximize_window()
# driver.minimize_window()
# driver.set_window_size(1000, 800)
driver.get("https://www.w3cschool.cn/")
'''浏览器向前、向后'''
driver.back()
driver.forward()
'''退出'''
driver.quit()
# driver.close()
# close()用于关闭当前窗口，quit()用于退出驱动程序并关闭所有相关窗口。
