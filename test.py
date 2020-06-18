
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