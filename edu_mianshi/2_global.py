'''
怎么在局部使用 全局变量
如果不加global则n是局部变量
'''

n = 3
def func():
    global n
    n = 5
    print(n)

func()
print(n)