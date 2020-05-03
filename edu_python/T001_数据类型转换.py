# int ---> bool
i = 100
print(bool(i))  # True  # 非零即True
i1 = 0
print(bool(i1))  # False 零即False

# bool ---> int
t = True
print(int(t))  # 1  True --> 1
t = False
print(int(t))  # 0  False --> 0

# int ---> str
i1 = 100
print(str(i1))  # '100'

# str ---> int  # 全部由数字组成的字符串才可以转化成数字
s1 = '90'
print(int(s1))  # 90

# str ---> bool
s1 = '太白'
s2 = ''
print(bool(s1))  # True 非空即True
print(bool(s2))  # False
# bool ---> str
t1 = True
print(str(True))  # 'True'

''' list  str ##################### '''
# str ---> list
s1 = 'alex 太白 武大'
print(s1.split())  # ['alex', '太白', '武大']

# list ---> str  # 前提 list 里面所有的元素必须是字符串类型才可以
l1 = ['alex', '太白', '武大']
print(' '.join(l1))  # 'alex 太白 武大'

'''list set#########################'''
# list ---> set
s1 = [1, 2, 3]
print(set(s1))

# set ---> list
set1 = {1, 2, 3, 3,}
print(list(set1))  # [1, 2, 3]

'''str   bytes#########################'''
# str ---> bytes
s1 = '太白'
print(s1.encode('utf-8'))  # b'\xe5\xa4\xaa\xe7\x99\xbd'

# bytes ---> str
b = b'\xe5\xa4\xaa\xe7\x99\xbd'
print(b.decode('utf-8'))  # '太白'

'''  转化成bool值为False的数据类型有：####### '''

'', 0, (), {}, [], set(), None

'''str ----> bytes######################'''
# encode称作编码:将 str 转化成 bytes类型
s1 = '中国'
b1 = s1.encode('utf-8')  # 转化成utf-8的bytes类型
print(s1)  # 中国
print(b1)  # b'\xe4\xb8\xad\xe5\x9b\xbd'

s1 = '中国'
b1 = s1.encode('gbk')  # 转化成gbk的bytes类型
print(s1)  # 中国
print(b1)  # b'\xd6\xd0\xb9\xfa'

'''bytes ---> str##########'''
# decode称作解码, 将 bytes 转化成 str类型
b1 = b'\xe4\xb8\xad\xe5\x9b\xbd'
s1 = b1.decode('utf-8')
print(s1)  # 中国