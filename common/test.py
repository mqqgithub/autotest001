def wrapper(func):
    def inner(*args, **kwargs):
        print(f'执行被装饰函数之前的操作')
        ret = func(*args, **kwargs)
        print(f'执行被装饰函数之后的操作')
        return ret
    return inner


def test(a):
    print(f'test{a}')
    return 'b'

t = wrapper(test)
print(t('1'))

