'''
一行代码实现1-100数据之和
分析：
'''

# sum()可迭代的对象
num = sum(range(1, 101))
print(num)

#
n = 0
for i in range(1, 101):
    n += i
print(n)
