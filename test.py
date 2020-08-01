
class A():

    singleton = None
    def __init__(self):
        print('aaaa')

    def __new__(cls, *args,  **kwargs):
        if cls.singleton is None:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton


a = A()
b = A()
print(id(a), id(b))

a = [1, 3, 10, 9, 21, 35, 4, 6]
s = range(1, len(a))[::-1]
print(list(s)) # 交换次数
for i in s:
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    print("第 %s 轮交换后数据：%s" % (len(s)-i+1, a))
print(a)