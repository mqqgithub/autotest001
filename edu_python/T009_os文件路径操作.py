import os

# 获取当前路径
print(os.getcwd())
# 获取操作系统
print(os.name)
# 获取环境变量
print(os.environ.get('path'))
# 获取当前的绝对路径
print(os.path.abspath(','))
# 路径拼接 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
#os.path.join('', '')
# 创建一个文件夹
#os.mkdir('')
# 删除一个文件夹
#os.rmdir()
# 拆分路径，把最后一个去掉
#os.path.split('')
# 删除文件
#os.remove('')
# 当前文件路径
print(os.path.abspath(__file__))
# 当前文件的上一路径
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.split(os.path.abspath(__file__))[0])
print(os.path.split(os.path.abspath(__file__))[1])
# os.path.split() 分离文件和文件夹
