# 如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。
class Father(object):
    def __init__(self, name):
        self.name = name
        print("name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name


class Son(Father):
    def getName(self):
        return 'Son ' + self.name

# 如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__
class Sons(Father):
    def __init__(self, name):
        print("hi")
        self.name = name
    def getName(self):
        return 'Sons '+self.name

# 如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
class Sonss(Father):
    def __init__(self, name):
        super(Sonss, self).__init__(name)
        # Father.__init__(self, name)
        print("hi")
        self.name =  name
    def getName(self):
        return 'Sonss  '+self.name


son = Son('qqq')
print(son.getName())
sons = Sons('www')
print(sons.getName())
sonss = Sonss('eee')
print(sonss.getName())

