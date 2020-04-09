# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明


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