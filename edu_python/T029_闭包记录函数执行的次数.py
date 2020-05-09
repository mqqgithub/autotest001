'''
闭包的定义：
    1. 闭包是嵌套在函数中的函数。
    2. 闭包必须是内层函数对外层函数的变量（非全局变量）的引用。
闭包的作用：
    1、保存局部信息不被销毁，保证数据的安全性。
闭包的应用：
    1、可以保存一些非全局变量但是不易被销毁、改变的数据。
    2、装饰器。
'''


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


avg = make_averager()
# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)
# 当然还有一些参数，仅供了解：
# 函数名.__code__.co_freevars 查看函数的自由变量
print(avg.__code__.co_freevars)  # ('series',)
# 函数名.__code__.co_varnames 查看函数的局部变量
print(avg.__code__.co_varnames)  # ('new_value', 'total')
# 函数名.__closure__ 获取具体的自由变量对象，也就是cell对象。
# (<cell at 0x0000020070CB7618: int object at 0x000000005CA08090>,)
# cell_contents 自由变量具体的值
print(avg.__closure__[0].cell_contents)  # []


def set_func(func):
    num = [0]   # 闭包中外函数中的变量指向的引用不可变

    def call_func():
        func()
        num[0] += 1
        print("执行次数", num[0])
        if num[0]%3 == 0:
            return 0
        if num[0]%3 == 1:
            return 1
        if num[0]%3 == 2:
            return 2

    return call_func

# 待测试方法
@set_func
def test():
    pass


print(test())
print(test())
print(test())
print(test())
print(test())
print(test())