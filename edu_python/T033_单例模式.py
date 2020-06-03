# https://www.cnblogs.com/huchong/p/8244279.html#_lab2_1_3
'''
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当
你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
例如：客户端通过一个 AppConfig 的类来读取配置文件的信息，配置文件很多系统都在用

'''

'''方式一
Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，
就会直接加载 .pyc 文件，而不会再次执行模块代码。
'''
'''方式二
使用装饰器
'''
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
print(a1)
a2 = A(3)
print(a2)

'''
通过new实现单例
'''
class Single(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

a = Single()
b = Single()
print(a)
print(b)


