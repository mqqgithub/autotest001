'''
可迭代对象：
    从字面意思来说：可迭代对象就是一个可以重复取值的实实在在的东西。
    从专业角度来说：但凡内部含有__iter__方法的对象，都是可迭代对象。
迭代器：
    在python中，内部含有'__Iter__'方法并且含有'__next__'方法的对象就是迭代器。
'''

o1 = 'alex'
o2 = [1, 2, 3]
o3 = (1, 2, 3)
o4 = {'name': '太白','age': 18}
o5 = {1, 2, 3}
f = open('file',encoding='utf-8', mode='w')
print('__iter__' in dir(o1))  # True
print('__iter__' in dir(o2))  # True
print('__iter__' in dir(o3))  # True
print('__iter__' in dir(o4))  # True
print('__iter__' in dir(o5))  # True
print('__iter__' in dir(f))  # True
# hsagn
print('__next__' in dir(o1))  # False
print('__next__' in dir(o2))  # False
print('__next__' in dir(o3))  # False
print('__next__' in dir(o4))  # False
print('__next__' in dir(o5))  # False
print('__next__' in dir(f))  # True
f.close()
# 通过以上代码可以验证，之前我们学过的这些对象，只有文件句柄是迭代器，剩下的那些数据类型都是可迭代对象。
# 可迭代对象如何转化成迭代器
l1 = [1, 2, 3, 4, 5, 6]
obj = l1.__iter__()  # 或者 iter(l1)print(obj)

# 迭代器取值：
l1 = [1, 2, 3,]
obj = l1.__iter__()  # 或者 iter(l1)
# print(obj)  # <list_iterator object at 0x000002057FE1A3C8>
ret = obj.__next__()
print(ret)
ret = obj.__next__()
print(ret)
ret = obj.__next__()
print(ret)
ret = obj.__next__()  # StopIteration
print(ret)
# 迭代器利用next取值：一个next取对应的一个值，如果迭代器里面的值取完了，还要next，
# 那么就报StopIteration的错误。


#