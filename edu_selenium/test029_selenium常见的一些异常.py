# 1。导入selenium包异常
# 现象：pycharm中输入from selenium import webdriver, selenium标红
# 原因 pycharm使用的虚拟环境中没有安装selenium； 前项目下有selenium.py,和系统包名冲突导致

# 2。驱动及本地服务类异常
# 未找到响应的浏览器驱动
# WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
# WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
# 原因: 查找不到对应的浏览器驱动
# 载浏览器对应版本的chromedriver
# 或geckodrivergeckodriver
# 放到脚本当前文件夹下或将路径配置到环境变量中,
# 或放到Python目录的Scripts下(一般情况下Python的Scripts目录在环境变量中),
# 或使用浏览器选项options指定驱动路径

# 3。未找到浏览器
# WebDriverException: Message Can not connect to the Service chromedriver
# org.openqa.selenium.WebDriverException: Failed to connect to binary FirefoxBinary
# 原因: 在默认路径下未找到Firefox浏览器
# 解决方法: 重新安装Firefox浏览器

# 4。驱动和浏览器不匹配
# SessionNotCreatedException: Message: session not created:
# this version of ChromeDriver only supports Chrome version 76
# 原因: 当前使用chromedriver只支持Chrome76版本
# 解决方法: 查看本地Chrome浏览器的版本, 下载对应的chromedriver

# 5。驱动被防火墙拦截
# WebDriverException: Message: Can not connect to the Service IEDriverServer.exe
# 原因: iedriverserver.exe被防火墙拦截
# 解决方法: 防火墙设置允许

# 6.连接不上chromedriver服务
# WebDriverException: Message: Can not connect ot the Service chromedriver
# 原因: 脚本通过127.0.0.1这个ip访问本地chromedriver服务, hosts中未配置 127.0.0.1指向localhost
# 解决办法: 配置本地hosts, 添加:127.0.0.1 localhost

# 7. RemoteDriverServerException: 远程服务器异常, 解决方法: 确认webdriver.Remote()中的远程Webdriver服务是否OK
# 8. ErrorInResponseException: Webdriver服务器响应异常, 解决方法, 根据具体报错信息分析

# 找不到类异常: 定位/获取属性/切换警告框,Frame, 窗口#
# NoSuchElementException: 找不到元素, 解决方法: 前面加上sleep等待后重试,或换一种定位方式
# NoSuchAttributeException: 元素没有这个属性, 解决方法: 确认定位到的元素是否目标元素, 检查属性拼写
# 3.NoAlertPresentException：没有找到alert弹出框, 解决方法: 观察页面,查看是否有弹框出现, 加上等待或作为偶现元素处理
# NoSuchFrameException：没有找到指定的frame或iframe, 解决方法: 查看拼写或切换使用frame的id/name/index/定位到的frame
# NoSuchWindowException: 没找到窗口句柄指定的窗口, 解决方法: 查看使用的窗口句柄变量拼写
# UnexpectedAlertPresentException: 出现了弹框而未处理, 解决方法: 切换到警告框并处理, 如果偶现,使用try...except处理偶现弹框
# InvalidSwitchToTargetException: 切换到指定frame或窗口报错, 解决方法: 查看相应的frame或窗口是否能定位到
# UnexpectedTagNameException: 使用Tag Name不合法, 解决方法: 检查拼写或使用css selector/xpath
# 9.TimeoutException：查找元素或操作超时, 解决方法, 稍后重试

# 元素操作异常类: 隐藏/不可操作状态#
# ElementNotVisibleException：元素不可见异常, selenium不能直接操作隐藏元素, 解决方法: 加上等待, 使用正常步骤使元素显示, 或使用js找到该元素的祖先节点的隐藏属性(通常为styple="display: none"), 移除该属性然后定位操作.
# StaleElementReferenceException: 陈旧元素引用异常, 页面刷新或跳转后使用了之前定位到的元素, 解决方法: 重新定位元素并操作
# InvalidElementStateException: 元素状态异常 元素只读/不可点击等, 解决方法, 等待或使用js移除元素readonly/disable等限制属性后操作
# ElementNotSelectableException：元素不可被选中, 解决方法: 确认原始是否为select标签, 是否禁用
# InvalidSelectorException: 使用的定位方法不支持或xpath语法错误, 未返回元素, 解决方法: 检查使用的元素定位器是否拆包, 使用find_element()方法是, 第一个参数为'class name', 'link text', 'particial link text' 'css selector', 空格分开, 非下划线连接, 建议使用By.CLASS_NAME的方式. 使用chrome开发着工具+Ctrl+F搜索验证自己写的xpath语法.
# MoveTargetOutOfBoundsException: 使用ActionChains的move方法时移动到的位置不合适

# Cookie存取相关异常#
# InvalidCookieDomainException: Cookie相应的域名无效
# UnableToSetCookieException: 设置Cookie异常
# IME输入法引擎异常#
# ImeNotAvailableException: 服务器不支持输入法
# ImeActivationFailedException: 输入法激活异常
