'''  统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]  '''
# 方法1
list1 = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
a = [i for i in list1 if i > 0]
print(len(a))
b = [i for i in list1 if i < 0]
print(len(b))
# 方法二
m = 0
n = 0
for i in list1:
    if i > 0:
        m += 1
    elif i < 0:
        n += 1
    else:
        pass
print(m, n)

'''  字符串 "axbyczdj"，如果得到结果“abcd”  '''
# 方法1：
s = 'axbyczdj'
s1 = s[::2]
print(s1)
# 方法2
l = []
for i in range(len(s)):
    if i % 2 == 0:
        l.append(s[i])
s2 = ''.join(l)
print(s2)

'''  已知一个字符串为“hello_world_yoyo”, 如何得到一个队列["hello","world","yoyo"]  '''
s = 'hello_world_yoyo'
l = s.split('_')
print(l)

'''  已知一个数字为 1，如何输出“0001”'''
a = 1
print('%04d' % a)

'''  已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]'''
a = [1, 3, 5, 7]
a.insert(3, a[0])
# a.pop(0)
# a.remove(1)
# del a[0]
print(a)

''' 已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9'''
# 方法1
a = 9
b = 8
a, b = b, a
# 方法2
c = a
a = b
b = c
print(a, b)

'''  打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
字立方和等于该数本身。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋
5 的三次方＋3 的三次方'''
sxh = []
for i in range(100, 1000):
    m = list(str(i))
    if i == int(m[0])**3+int(m[1])**3+int(m[2])**3:
        sxh.append(i)
print('水仙数', sxh)

'''如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备
数。 例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余
3 个数相加，
1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28
外，其余 5 个数相加，1+2+4+7+14=28。
那么问题来了，求 1000 以内的完全数有哪些？'''
wqs = []
for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s = s+j
    if s == i:
        wqs.append(i)
print('完全数', wqs)

'''用 python 写个冒泡排序 a = [1, 3, 10, 9, 21, 35, 4, 6]'''
a = [1, 3, 10, 9, 21, 35, 4, 6]
n = len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print(a)
print(a)

'''  sort排序 已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]   正序、倒序、去重复  '''
a = [1, 3, 6, 9, 7, 3, 4, 6]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b = list(set(a))
print(b)

''' 阶乘3*2*1 '''

def xxx(x):
    if x == 1:
        return 1
    return x * xxx(x-1)

print(xxx(9))

'''斐波那契数列  已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都
等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据'''
a = 0
b = 1
while b < 100:
    print(b, end=',')
    a, b = b, a+b
print('\n')

'''  幂的递归  计算 x 的 n 次方，如：3 的 4 次方 为 3*3*3*3=81 '''
def yyy(x, n):
    if n == 0:
        return 1
    else:
        return x*yyy(x, n-1)

print(yyy(3, 5))

''' 汉诺塔 把a上的圆盘都挪到c上，每次只能拿一个，只能吧小的盘子放在大盘子上'''

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        print(a, '-->', c)
        hanoi(n-1, b, a, c)

hanoi(2, 'A', 'B', 'C')

