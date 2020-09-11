# 浏览器的相关操作
from selenium import webdriver

'''需要能找到驱动的位置，也可以在环境变量中'''
driver = webdriver.Chrome(r"D:\Program Files\Python37\chromedriver.exe")
# jenkins执行脚本的时候可能需要驱动和浏览器在同一个目录，不然会提示找不到浏览器，考虑加环境变量
# driver = webdriver.Chrome("C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
# driver = webdriver.Chrome()
# driver = webdriver.Ie()
# driver = webdriver.Firefox()


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

'''刷新'''
driver.refresh()

'''浏览器的名字'''
n = driver.name
print(n)

'''截图'''
# driver.get_screenshot_as_base64()  # html文件界面会用到
# driver.get_screenshot_as_file(r"D:\test.jpg")
# driver.save_screenshot(r"D:\test.jpg")  # 同上2个一样的

'''退出'''
driver.quit()
# driver.close()
# close()用于关闭当前窗口，quit()用于退出驱动程序并关闭所有相关窗口。


'''
用Chrome地址栏输入chrome://version/，查看自己的“个人资料路径”，然后在浏览器启动时，调用这个配置文件，代码如下：
　　#coding=utf-8
　　from selenium import webdriver
　　option = webdriver.ChromeOptions()
    # 默认使用个人浏览器设置
　　# option.add_argument(r'--user-data-dir=C:\   Users\Administrator\AppData\Local\Google\Chrome\  User Data') #设置成用户自己的数据目录
　　# 设置默认大小
    # option.add-argument(r'--window-size=1366,768')
    # 无界面运行
    # option.add-argument(r'--headless')
    # 最大化运行
    # option.add-argument('--start-maximized')
    # 禁用自动化测试
    # option.add-argument('--disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
'''
