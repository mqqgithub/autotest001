from selenium import webdriver
import logging


logging.basicConfig(level=logging.DEBUG)  # 打印源码中的日志
dr = webdriver.Chrome() # 打开浏览器
dr.get("https://www.cnblogs.com/linuxchao/") # 访问我的博客首页