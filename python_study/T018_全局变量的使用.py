'''
局部变量:
局部变量是指在函数内部定义并使用的变量，它只在函数内部有效。
每个函数在执行时，系统都会为该函数分配一块“临时内存空间”，所有的局部变量都被保存在这块临时内存空间内。
当函数执行完成后，这块内存空间就被释放了，这些局部变量也就失效了，
因此离开函数之后就不能再访问局部变量了，否则解释器会抛出
'''
def text1():
    demo = 'C语言中文网'
    print(demo)
text1()
#此处获取局部变量值会引发错误
# print('局部变量 demo 的值为：',demo) # 会报错

'''
全局变量：
全局变量指的是能作用于函数内外的变量，即全局变量既可以在各个函数的外部使用，也可以在各函数内部使用。
1、在函数体外定义的变量，一定是全局变量
2、在函数体内定义全局变量。即使用 global 关键字对变量进行修饰后，该变量就会变为全局变量
'''

#在函数体外定义的变量，一定是全局变量
demo = "C语言中文网"
def text2():
    print("函数体内访问：", demo)
text2()
print('函数体外访问：', demo)

# 在函数体内定义全局变量。即使用 global 关键字对变量进行修饰后，该变量就会变为全局变量
# 注意，在使用 global 关键字修饰变量名时，不能直接给变量赋初值，否则会引发语法错误。
def text3():
    global demo
    demo = "C语言中文网"
    print("函数体内访问：", demo)
text3()
print('函数体外访问：', demo)
