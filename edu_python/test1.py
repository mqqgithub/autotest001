# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;

from selenium import webdriver


def get_driver(host):
    lists = {'http://192.168.170.78:4444/wd/hub': 'chrome',
             'http://192.168.170.78:5555/wd/hub': 'chrome',
             'http://192.168.170.78:6666/wd/hub': 'chrome'
             }
    ip1 = "http://192.168.170.78:4444/wd/hub"
    ip2 = ""
    if host == 1:
        driver = webdriver.Remote(command_executor=ip1, desired_capabilities="chrome")
    return driver

def set_func(func):
    num = [0]   # 闭包中外函数中的变量指向的引用不可变
    def call_func():
        func()
        num[0] += 1
        print("执行次数", num[0])
        t = num[0]%3
        if t == 0:
            get_driver(list)
        if t == 1:
            return 1
        if t == 2:
            return 2

    return call_func

# 待测试方法
@set_func
def test():
    pass

if __name__  == "__main__":
    print(test())
    print(test())
    print(test())
    print(test())
    print(test())
    print(test())