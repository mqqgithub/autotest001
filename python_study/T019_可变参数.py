'''
单个 *
如：*parameter是用来接受任意多个参数并将其放在一个元组中。
'''
def test1(*a):
    print(*a)
    print(a)
    print(type(a))

test1(1, 3, 2)
test1(*(1, 11, 111))
test1((2, 22, 222))


'''
函数在调用多个参数时，在列表、元组、集合、字典及其他可迭代对象作为实参，并在前面加 *
提示：序列解包要在关键参数和  **参数 之前进行处理
'''
def test2(x,y,z):
    print(x, y, z)
    print(x)
    print(y)
    print(z)


test2(1, 2, 3)
test2(*(1, 1, 1))
test2(*[2, 2, 2])
test2(*{'x': 1, 'y': 2, 'z': 3}) # 解包取的是键值

'''
两个 **  
如:**parameter用于接收类似于关键参数一样赋值的形式的多个实参放入字典中（即把该函数的参数转换为字典）
'''
def test3(**kwargs):
    for i in kwargs.items():
        print(i)


test3(x=1, y=2, z=3)
test3(**{'x': 1, 'y': 2, 'z': 3})