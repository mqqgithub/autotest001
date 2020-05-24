'''webdriver  原理：
1. WebDriver 启动目标浏览器，并绑定到指定端口。该启动的浏览器实例，做为 web driver 的 remote
server。
2. Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： the
webriver wire protocol）
3. Remote server 需要依赖原生的浏览器组件（如：IEDriverServer.exe、chromedriver.exe），来转
化转化浏览器的 native 调用。

在 Python 提供了 logging 模块，logging 模块给运行中的应用提供了一个标准的信息输出接口。它
提供了 basicConfig()方法用于基本信息的定义。将 debug 模块开启。就可以捕捉到客户端与服务器的交互信息。
'''

# https://www.cnblogs.com/uncleyong/p/11898297.html


from selenium import webdriver
import logging
logging.basicConfig(level=logging.DEBUG)
diver = webdriver.Chrome()
diver.get("http://www.baidu.com")
diver.find_element_by_id("kw").send_keys("selenium")
diver.find_element_by_id("su").click()
diver.quit()

