'''
list.append()
list()
list.insert()
list.extend()
list.pop()
list.remove()
list.clear()
del list[]  切片
list.sort() 只打印，无返回值，改变了原来的值
list.reverse()
li = sort(list)  产生新的值
li = reverse(list)
'''



'''  创建一个列表有三种方式  '''
# 方式一：（常用）
l1 = [1, 2, '太白']

# 方式二：（不常用）
l2 = list()  # 空列表

# l1 = list(iterable)  # 可迭代对象
l3 = list('123')
print(l1)  # ['1', '2', '3']

# 方式三：列表推导式（后面的课程会讲到）
l4 = [i for i in range(1, 5)]
print(l1)  # [1, 2, 3, 4]

''' 列表中增加数据  '''
# append 追加，给列表的最后面追加一个元素
l = [1, 2, 'a']
l.append(666)
print(l)  # [1, 2, 'a', 666]

# insert  插入在列表的任意位置插入元素
l = [1, 2, 'a']
l.insert(1, '太白')
print(l)  # [1, '太白', 2, 'a']

print('extend  迭代着追加，在列表的最后面迭代着追加一组数据')
l = [1, 2, 'a']
l.extend('太白a')
l.extend(['q', 'w', 'e'])
print(l)

'''  列表删除    '''
print('pop  通过索引删除列表中对应的元素，该方法有返回值，返回值为删除的元素')
l = ['太白', 'alex', 'WuSir', '女神']
ret = l.pop(1)
print(ret, l)  # alex ['太白', 'WuSir', '女神']

print('remove  通过元素删除列表中该元素')
l = ['太白', 'alex', 'WuSir', '女神']
l.remove('alex')
print(l) # ['太白', 'WuSir', '女神']

print('clear 清空列表')
l = ['太白', 'alex', 'WuSir', '女神']
l.clear()
print(l) # []

# del
print('按照索引删除该元素')
l = ['太白', 'alex', 'WuSir', '女神']
del l[2]
print(l)  # ['太白', 'alex', '女神']

print('切片删除该元素')
l = ['太白', 'alex', 'WuSir', '女神']
del l[1:]
print(l)  # ['太白']

print('切片(步长)删除该元素')
l = ['太白', 'alex', 'WuSir', '女神']
del l[::2]
print(l)  # ['alex', '女神']

'''  列表的改   '''
print('按照索引改值')
l = ['太白', 'alex', 'WuSir', '女神']
l[0] = '男神'
print(l)  # ['男神', 'alex', 'WuSir', '女神']

print('按照切片改值(迭代着增加)')
l = ['太白', 'alex', 'WuSir', '女神']
l[1:3] = 'abcdefg'
print(l)  # ['太白', 'a', 'b', 'c', 'd', 'e', 'f', 'g', '女神']

print('按照切片(步长)改值(必须一一对应)')
l = ['太白', 'alex', 'WuSir', '女神']
l[::2] = '对应'
print(l)  # ['对', 'alex', '应', '女神']

''' count index     '''
a = ["q", "w", "q", "r", "t", "y"]
print('count', a.count("q"))

a = ["q","w","r","t","y",'r']
print('index', a.index("r"))

a = [2, 1, 3, 4, 5]
a.sort()  # 他没有返回值，所以只能打印a
print('sort', a)
a.reverse()  # 他也没有返回值，所以只能打印a
print('reverse', a)

''' 相加、相乘  '''
l11 = [1, 2, 3]
l21 = [4, 5, 6]
print('相加', l1+l2)  # [1, 2, 3, 4, 5, 6]
print('相乘', l1*3)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
