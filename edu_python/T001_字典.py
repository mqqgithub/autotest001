''' 创建字典 '''

print('dict转化列表元组')
l1 = dict((('a', 1), ('b', 2), ('c', 3)))
print(l1)
l2 = dict([('a', 1), ('b', 2), ('c', 3)])
print(l2)

print('dict 键值对')
l3 = dict(a=1, b=2, c=3)
print(l3)

print('zip')
l4 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print('l4', l4)

print("推导式")
dic = {k: v for k, v in [('one', 1), ('two', 2), ('three', 3)]}
print('dic', dic)

print('fromkeys 字符串')
dic = dict.fromkeys('abcd','太白')
print(dic)  # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}


'''  字典的增  '''
print('通过键值对直接增加')
dic1 = {'name': '太白', 'age': 18}
dic1['weight'] = 75  # 没有weight这个键，就增加键值对
print(dic)  # {'name': '太白', 'age': 18, 'weight': 75}
dic1['name'] = 'barry'  # 有name这个键，就成了字典的改值
print(dic1)  # {'name': 'barry', 'age': 18, 'weight': 75}

print('setdefault')
dic = {'name': '太白', 'age': 18}
dic.setdefault('height', 175)  # 没有height此键，则添加
print(dic)  # {'name': '太白', 'age': 18, 'height': 175}
dic.setdefault('name', 'barry')  # 有此键则不变
print(dic)  # {'name': '太白', 'age': 18, 'height': 175}

print('它有返回值')
dic = {'name': '太白', 'age': 18}
ret = dic.setdefault('name')
print(ret)  # 太白

'''  字典的删 '''
# pop 通过key删除字典的键值对，有返回值，可设置返回值。
dic = {'name': '太白', 'age': 18}
# ret = dic.pop('name')
# print(ret,dic) # 太白 {'age': 18}
ret1 = dic.pop('n', None)
print(ret1, dic)  # None {'name': '太白', 'age': 18}

# popitem 3.5版本之前，popitem为随机删除，3.6之后为删除最后一个，有返回值
dic = {'name': '太白', 'age': 18}
ret = dic.popitem()
print(ret, dic)  # ('age', 18) {'name': '太白'}

# clear 清空字典
dic = {'name': '太白', 'age': 18}
dic.clear()
print(dic)  # {}

# del
# 通过键删除键值对
dic = {'name': '太白', 'age': 18}
del dic['name']
print(dic) # {'age': 18}
# 删除整个字典
del dic

'''   字典的改 '''
print('通过键值对直接改')
dic = {'name': '太白', 'age': 18}
dic['name'] = 'barry'
print(dic)  # {'name': 'barry', 'age': 18}

print('update')
dic = {'name': '太白', 'age': 18}
dic.update(sex='男', height=175)
print(dic) # {'name': '太白', 'age': 18, 'sex': '男', 'height': 175}

dic = {'name': '太白', 'age': 18}
dic.update([(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')])
print(dic)  # {'name': '太白', 'age': 18, 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dic1 = {"name": "jin", "age": 18, "sex": "male"}
dic2 = {"name": "alex", "weight": 75}
dic1.update(dic2)
print(dic1)  # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
print(dic2)  # {'name': 'alex', 'weight': 75}

''' 字典的查   '''
# 通过键查询
# 直接dic[key](没有此键会报错)
dic = {'name': '太白', 'age': 18}
print(dic['name']) # 太白

# get
dic = {'name': '太白', 'age': 18}
v = dic.get('name')
print(v) # '太白'
v = dic.get('name1')
print(v) # None
v = dic.get('name2','没有此键')
print(v) # 没有此键


# keys()
dic = {'name': '太白', 'age': 18}
print(dic.keys())  # dict_keys(['name', 'age'])

# values()
dic = {'name': '太白', 'age': 18}
print(dic.values())  # dict_values(['太白', 18])

# items()
dic = {'name': '太白', 'age': 18}
print(dic.items())  # dict_items([('name', '太白'), ('age', 18)])

'''  fromkeys'''
ic = dict.fromkeys('abcd','太白')
print(dic) # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}

dic = dict.fromkeys([1, 2, 3],'太白')
print(dic) # {1: '太白', 2: '太白', 3: '太白'}

'''   '''
key_list = dic.keys()
print(key_list)
'''
结果:
dict_keys(['剑圣', '哈啥给', '大宝剑'])'''
# 一个高仿列表,存放的都是字典中的key

# 并且这个高仿的列表可以转化成列表
print(list(key_list))

# 它还可以循环打印

dic = {'剑圣':'易','哈啥给':'剑豪','大宝剑':'盖伦'}

for i in dic:
    print(i)



value_list = dic.values()
print(value_list)
'''
结果:
dict_values(['易', '剑豪', '盖伦'])'''
#一个高仿列表,存放都是字典中的value
# 并且这个高仿的列表可以转化成列表
print(list(value_list))

# 它还可以循环打印
for i in dic.values():
    print(i)


key_value_list = dic.items()
print(key_value_list)
'''
结果:
dict_items([('剑圣', '易'), ('哈啥给', '剑豪'), ('大宝剑', '盖伦')]'''

# 一个高仿列表,存放是多个元祖,元祖中第一个是字典中的键,第二个是字典中的值　　

# 并且这个高仿的列表可以转化成列表
print(list(key_value_list ))

# 它还可以循环打印
dic = {'剑圣':'易','哈啥给':'剑豪','大宝剑':'盖伦'}
for i in dic.items():
    print(i)
''''结果：
('剑圣', '易')
('哈啥给', '剑豪')
('大宝剑', '盖伦')'''

''' 拆包 '''

a,b = 1,2
print(a,b)


a,b = ('你好','世界')  # 这个用专业名词就叫做元组的拆包
print(a,b)

a,b = ['你好','大飞哥']
print(a,b)

a,b = {'汪峰':'北京北京','王菲':'天后'}
print(a,b)

''' 键值对'''
for k,v in dic.items():
    print('这是键',k)
    print('这是值',v)