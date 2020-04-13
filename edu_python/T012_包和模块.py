# import module   只能引用模块
# 导入模块的所有成员，但是要使用模块成员是不许加上模块.的形式

# from  package.module  import class/fuction
# 导入具体的成员，可以直接使用

# from  package.module  import  *
# 导入所有成员，不推荐使用这种写法，因为如果有2个模块含有相同的方法名，就是分不清
# 每个模块下面都有__init__.py文件,定义__all__ = ['os', 'sys', 're', 'urllib']实际导入的是这些,如果没有维护，则没有导入
'''
通常情况下，当使用 import 语句导入模块后，Python 会按照以下顺序查找指定的模块文件：
在当前目录，即当前执行的程序文件所在目录下查找；
到 PYTHONPATH（环境变量）下的每个目录中查找；
到 Python 默认的安装目录下查找。
'''