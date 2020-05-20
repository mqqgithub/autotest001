from edu_python.T001 import Test001


class Test(Test001):
    def __init__(self, x):
        super().__init__(x)
        print('init我是引用者', x)

    def test(self):
        t1 = Test001(1)
        print('t1', t1)


if __name__ == "__main__":
    t = Test('ooooo')
    t.test()
