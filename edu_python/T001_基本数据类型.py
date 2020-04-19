# Python基本数据类型
# Number(数字)--int\float\bool\complex
# string(字符串)
# List(列表)--有序
# Tuple(元组)--有序
# Sets(集合)--无序
# Dict(字典)--无序

# Number ################################################
i = 1
print('数字：%d' % i)  # 如果不是string的不能直接用+，必须用占位符%d数字  %s代表字符串
print(type(i))
f = 1.2
print(type(f))
b = True
print(type(b))


a = 5
b = 3
print(a/b)  # 返回浮点型
print(a//b)  # 取整数
print(a % b)  # 取余数
print(a**b)  # 平方

# string ################################################
# 元素是不可变的

string = 'abcdefg'
print(string)
print(string[0])
print(string[0:-1])  # 从头到尾
print(string[2:])  # 从下标2开始到尾
print(string[2:4])  # 从下标2到n-1  [m,n)
print(string*2)  # 输出2次


#  list ###############################################
# 元素可变的
listDemo = ["aa", 1, "bb", 2]
print(listDemo)
print(listDemo[0])  # 输出下标0
print(listDemo[2:])  # 从下标2开始到尾
print(listDemo[1:3])  # 从下标2到n-1  [m,n)
print(listDemo*2)  # 输出2次
listDemo[0] = "替换的"
print(listDemo)  # 修改后的


# 此方法不返回任何值，但从列表中反转给定对象。string,tuple no reverse()
def variablenumbers():
    lis = [x for x in range(101)]
    lis.reverse()
    lis2 = lis[0:-1:8]
    print('====', lis2)
variablenumbers()
listDemo = ["one", "two", "three", "four", "five"]
listDemo.insert(0, "insert")
listDemo[0] = "update"
del listDemo[0]

print("len(listDemo) %r" % (len(listDemo)))
print("max(listDemo) %r" % (max(listDemo)))
print("min(listDemo) %r" % (min(listDemo)))
print("listDemo.sort() %r" % (listDemo.sort()))
print("排序后", listDemo)

#list.copy() 复制
#删除
#list.pop(index)
#list.remove(value)

# tuple ###############################################
# 元祖不可变
tupleDemo =("aa", 1, "bb", 2)
print(tupleDemo)
print(tupleDemo[0])#输出下标0
print(tupleDemo[2:])#从下标2开始到尾
print(tupleDemo[1:3])#从下标2到n-1  [m,n)
print(tupleDemo*2)#输出2次

tupleDemo = ()#空元组
tupleDemo = ('a',)#一个元素
print(tupleDemo)
tup1 = (1, 2)
tup2 = ()
# 创建一个元素 一定要用 ,
tup3 = (4,)
# 修改元组 元组里面的元素是不允许修改的
# 修改是非法的,无效的
# tup1[0] = "update"
tup1 = tup1 + tup3
# 删除元组
# del tup1
print("len(tup1) ", len(tup1))
# max min
# tuple(list) 将列表转元组

# Set(集合) ###############################
# 一个无序不可重复的序列
setDemo = {"a", "b", 1}
print("集合A ", setDemo)
# 集合可以做 交集并集差集
setDemo2 = {"a", "b"}
print("集合B ", setDemo2)
print("AB的差集 ", setDemo - setDemo2)
print("AB的并集 ", setDemo | setDemo2)
print("AB的交集 ", setDemo & setDemo2)
print("AB的不同时存在的 ", setDemo ^ setDemo2)


#  字典 #####################################
dictDemo = {"tom": "90", "jerry": "75"}
print(dictDemo)
print(dictDemo["tom"])
print("keys:", dictDemo.keys())
print("values", dictDemo.values())
# 移除 key 返回value
print("移除tom ", dictDemo.pop("tom"))
print(dictDemo)
dict12 = {"tom": "90", "jerry": "75"}
dict12["sex"] = "男"
dict12["sex"] = "male"
del dict12["sex"]
# 清空
# dict1.clear()

print('{name} 和 {url}'.format(name='百度网站:', url='www.baidu.com'))

#python常用数据转换
'''
int(x)
str(x)
tuple(s) 将序列转换成元组
list(s) 将序列转换成列表

可变类型（mutable）：列表，字典
不可变类型（unmutable）：数字，字符串，元组
这里的可变不可变，是指内存中的那块内容（value）是否可以被改变
'''