'''
所以装饰器最终最完美的定义就是：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。
def wrapper(func):
    def inner(*args,**kwargs):
        #执行被装饰函数之前的操作
        ret = func
        #执行被装饰函数之后的操作
        return ret
    return inner
'''

login_status = {
    'username': None,
    'status': False,
}
def auth(x):
    def auth2(func):
        def inner(*args, **kwargs):
            if login_status['status']:
                ret = func()
                return ret

            if x == 'wechat':
                username = input('请输入用户名：').strip()
                password = input('请输入密码：').strip()
                if username == '太白' and password == '123':
                    login_status['status'] = True
                    ret = func()
                    return ret
            elif x == 'qq':
                username = input('请输入用户名：').strip()
                password = input('请输入密码：').strip()
                if username == '太白' and password == '123':
                    login_status['status'] = True
                    ret = func()
                    return ret

        return inner

    return auth2


@auth('wechat')
def jitter():
    print('记录美好生活')


@auth('qq')
def pipefish():
    print('期待你的内涵神评论')