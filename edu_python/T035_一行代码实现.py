# 1到100之和
print(sum(range(1, 101)))

# 数值交换
a = 1
b = 2
a, b = b, a

# 求奇偶数
print([x for x in range(1, 100) if x % 2 ==0])

# 二维列表变为一维列表
l1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print([j for i in l1 for j in i])

# 反转字符串
s = 'abc123'
print(s[::-1])

# 查看目录下的所有文件
import os
print(os.listdir('.'))

# 去掉字符串中的空格
s = 'aa bb cc'
print(s.replace(' ', ''))
print(''.join(s.split(' ')))

# 字符串列表变整数列表
l2 = ['1', '2', '3']
print([int(i) for i in l2])
print([a for a in map(lambda i: int(i), l2)])

# 除去列表中的重复值
l3 = [1, 2, 2, 3]
print(list(set(l3)))

# 一行代码实现99乘法表
print('\n'.join([' '.join(["%s*%s=%s" % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]))

# 字典排序
d = {'a': 1, 'c': 2, 'b': 3}
l1 = sorted(d.items(), key=lambda x: x[0], reverse=False)
l2 = sorted(d.items(), key=lambda x: x[1], reverse=False)
d = dict(l1)
d2 = dict(l2)
print(d)
print(d2)

