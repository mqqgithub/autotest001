'''  富文本使用js '''
from selenium import webdriver
import time


def rich_text(content):
    js = "document.getElementById('su').contentWindow.document.body.innerHTML='{0}'".format(content)
    return js


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
j = rich_text('文本笨笨额笨笨')
driver.execute_script(j)
driver.quit()










