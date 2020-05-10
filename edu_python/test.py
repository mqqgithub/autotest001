def func():
    print("111")
    yield 222
    print("333")
    yield 444

gener = func()

ret = gener.__next__()
print(ret)

ret2 = gener.__next__()
print(ret2)
ret3 = gener.__next__()
# 最后⼀个yield执⾏完毕. 再次__next__()程序报错
print(ret3)
