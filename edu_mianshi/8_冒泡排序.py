a = [1, 3, 10, 9, 21, 35, 4, 6]
l = len(a)
b = 0
for i in range(l-1):
    for j in range(l-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            b += 1
            print(b, a)

# 需要l-1轮排序
# 每轮需要l-1-i次比较
