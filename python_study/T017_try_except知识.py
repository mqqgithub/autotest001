'''

'''
def foo():
    try:
        fis = open("a.txt");
    except Exception as e:
        # 访问异常的错误编号和详细信息
        print(e.args)
        # 访问异常的错误编号
        print(e.errno)
        # 访问异常的详细信息
        print(e.strerror)
foo()

'''

'''
def test():
    s = input('请输入除数:')
    try:
        result = 20 / int(s)
        print('20除以%s的结果是: %g' % (s, result))
    except ValueError:
        print('值错误，您必须输入数值')
    except ArithmeticError:
        print('算术错误，您不能输入0')
    else:
        print('没有出现异常')
    print("程序继续运行")

test()