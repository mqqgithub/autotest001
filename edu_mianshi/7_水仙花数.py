'''
打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
字立方和等于该数本身。例如： 153 是一个"水仙花数"，因为 153=1 的三次方＋
5 的三次方＋ 3 的三次方

'''

a = []
for i in range(100, 1000):
    s1 = str(i)
    y = 0
    for s in s1:
        x = int(s)
        y += x**3
    if y == i:
        a.append(i)
print(a)
