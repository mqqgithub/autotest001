'''
怎么在局部修改 全局变量
如果不加global 则n是局部变量
'''

n = 3
def func():
    global n
    n = n-5
    print(n)

func()
print(n)