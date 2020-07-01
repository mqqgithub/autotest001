'''webdriver  原理：
1. WebDriver 脚本启动浏览器驱动创建server端，连接server端，并启动浏览器。
2. Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： the
webriver wire protocol）
3. Remote server 需要依赖原生的浏览器组件（如：IEDriverServer.exe、chromedriver.exe），来转
化转化浏览器的 native 调用。

python脚本--webdriver API--启动chromedriver.exe作为server端  （可以直接手动cmd运行chromedriver.exe）
python脚本--webdriver API--（转为post请求）--给server，返回session--打开浏览器
python脚本--webdriver API--（转为post请求带session）--给server--操作浏览器
session 是标记具体打开的那个浏览器
'''

# https://www.cnblogs.com/uncleyong/p/11898297.html
# https://www.cnblogs.com/linuxchao/p/linux-selenium-webdriver.html

import requests

# 请求地址(打开浏览器)
driver_url = 'http://localhost:9515/session'
# 打开浏览器的请求参数
driver_value = {"capabilities":
                    {"firstMatch": [{}],
                     "alwaysMatch":
                         {"browserName": "chrome",
                          "platformName": "any",
                          "goog:chromeOptions": {"extensions": [], "args": []}}},
                "desiredCapabilities":
                    {"browserName": "chrome",
                     "version": "",
                     "platform": "ANY",
                     "goog:chromeOptions": {"extensions": [], "args": []}}}
# 发送求清
response_session = requests.post(driver_url, json=driver_value)
print(response_session.json())
# 访问我的博客的请求地址 （这个地址是我们上面记录的地址）
url = 'http://localhost:9515/session/' + response_session.json()['sessionId'] + '/url'
# 访问我的博客的请求参数
value = {"url": "https://www.cnblogs.com/linuxchao/", "sessionId": response_session.json()['sessionId']}
response_blog = requests.post(url=url, json=value)
print(response_blog.json())
######
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
diver = webdriver.Chrome()
diver.get("http://www.baidu.com")
diver.find_element_by_id("kw").send_keys("selenium")
diver.find_element_by_id("su").click()
diver.quit()
