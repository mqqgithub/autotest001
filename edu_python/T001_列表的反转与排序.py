
l = [1, 2, 3, 5, 4]
# 改变了原来的值
l.reverse()
print(l)
# 创建了一个新的对象
m = list(reversed(l))
print("m", m)
l.sort()
print("l", l)
n = sorted(l)
print('n', n)
# 切片排序
# m = l[::-1]
''' 使用循环'''
m = []
while len(l)>0:
    m.append(l.pop())

'''

'''
print([i for i in m])
print(l)
