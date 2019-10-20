# python 的变量命名规范，类名单词首字母大写，其他均用小写单词加下划线


# 函数传参的问题
def sum1(x, y):
    print(x + y)
def sum2(*args):
    su = 0
    for i in range(len(args)):
        su += args[i]
    print(su)
def sum3(**kvargs):
    for i in kvargs:
        print(kvargs[i])


sum1(1, 2)
sum2(1, 2, 3)
sum3(a=1, b=2, c=3)
