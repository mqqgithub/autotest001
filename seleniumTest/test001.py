#浏览器的相关操作
from selenium import webdriver
#driver = webdriver.Chrome("D:\\TOOLS\jenkins\\browser_driver\\chromedriver.exe")
#driver = webdriver.Chrome("C:\\Users\\maqingqing\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.set_window_size(1000, 800)
driver.get("https://www.w3cschool.cn/")
driver.back()
driver.forward()
driver.quit()
#driver.close()
# close()用于关闭当前窗口，quit()用于退出驱动程序并关闭所有相关窗口。
