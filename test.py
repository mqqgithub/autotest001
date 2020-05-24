class A(object):
    def __init__(self):
        print('aaaaa')

    def test(self):
        print('from A')

class B(A):
    def __init__(self):
        print('bbbbb')

    def test(self):
        print('from B')

class C(A):
    #def __init__(self):
        #print('ccccc')

    def test(self):
        print('from C')

class D(B):
    def __init__(self):
        print('ddddd')

    def test(self):
        print('from D')

class E(C):
    def __init__(self, i):
        print('eeeee',i)

    def test(self):
        print('from E')


class F(E, D):
    # def test(self):
    #     print('from F')
    pass

f1 = F(1)
