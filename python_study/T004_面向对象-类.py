# 数据成员=类变量、实例变量
# 对象：通过类定义的数据结构实例。对象包括  两个数据成员（类变量和实例变量）  和     方法
class Student():
    # 类变量
    name = '张'
    age = 0

    # self代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。\\
    # 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性 ，实例变量、局部变量
        self.name = name
        self.age = age


student1 = Student("王", 2)
print(student1.name)
print(Student.name)
# 通过这个例子，能看出来实例化的时候，类变量并没有改变。self代表的是当前的实例，所以和self.变量总是实例变量

# 类的私有属性:__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
#     类的方法:在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
# 类的私有方法:private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print
        self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量
print(counter._JustCounter__secretCount) # Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
#
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# 
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。


