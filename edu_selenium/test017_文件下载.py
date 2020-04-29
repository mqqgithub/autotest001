# 下载文件

import os
from selenium import webdriver

'''firefox
browser.download.folderList设置为0表示文件下载到浏览器默认下载路径，为2表示下载到指定目录
browser.download.dir用于指定下载文件的目录。通过os.getcwd()方法获取当前文件所在位置，即下载文件保存的目录。
指定要下载的文件类型，即Content-type值
通过"binary/octet-stream"表示二进制文件
'''
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()

'''chrome
download.default_directory设置文件下载目录
'''
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()
