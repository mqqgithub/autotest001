a = 'ABCDEFGHIJK'
print(a[0:3])  # print(a[:3]) 从开头开始取0可以默认不写
print(a[2:5])
print(a[:]) #默认到最后
print(a[:-1]) # -1 是列表中最后一个元素的索引，但是要满足顾头不顾腚的原则，所以取不到K元素
print(a[:5:2]) #加步长
print(a[-1:-5:-2]) #反向加步长

'''数字符串中的元素出现的个数'''
ret3 = a.count("a", 0, 4)  # 可切片
print(ret3)

a4 = "dkfjdkfasf54"
# startswith 判断是否以...开头
# endswith 判断是否以...结尾
# ret4 = a4.endswith('jdk',3,6)  # 顾头不顾腚
# print(ret4)  # 返回的是布尔值
# ret5 = a4.startswith("kfj",1,4)
# print(ret5)

# split 以什么分割，最终形成一个列表此列表不含有这个分割的元素。
# ret9 = 'title,Tilte,atre,'.split('t')
# print(ret9)
# ret91 = 'title,Tilte,atre,'.rsplit('t',1)
# print(ret91)

# format的三种玩法 格式化输出
res = '{} {} {}'.format('egon', 18,' male')
print('res', res)
res1 = '{1} {0} {1}'.format('egon', 18, 'male')
print('res1', res1)
res2 = '{name} {age} {sex}'.format(sex='male', name='egon', age=18)
print('res2', res2)

# strip
name = '*barry**'
print(name.strip('*'))
print(name.lstrip('*'))
print(name.rstrip('*'))

# replace
name='alex say :i have one tesla,my name is alex'
print(name.replace('alex','SB',1))

# ####is系列
name = 'taibai123'
print(name.isalnum())  # 字符串由字母或数字组成
print(name.isalpha())  # 字符串只由字母组成
print(name.isdecimal())  # 字符串只由十进制组成


'''下面这些方法在数据类型补充时会讲到，现在不讲'''
# 寻找字符串中的元素是否存在
# ret6 = a4.find("fjdk",1,6)
# print(ret6)  # 返回的找到的元素的索引，如果找不到返回-1

# ret61 = a4.index("fjdk",4,6)
# print(ret61) # 返回的找到的元素的索引，找不到报错。

# captalize,swapcase,title
print(name.capitalize())  # 首字母大写
print(name.swapcase())  # 大小写翻转
msg = 'taibai say hi'
print(msg.title())  # 每个单词的首字母大写

# 内同居中，总长度，空白处填充
a1 = '12345'
ret2 = a1.center(20, "*")
print(ret2)
