# open函数最常用的使用方法如下：文件句柄 = open('文件路径', '模式'，编码方式)。
# r    以只读方式打开文件。这是默认模式。文件必须存在，不存在抛出错误
# rb   以二进制格式打开一个文件用于只读。
# r+   打开一个文件用于读写。文件指针将会放在文件的开头。读完就追加。
# w     打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+  打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# 注：后面有带b的方式，不需要考虑编码方式。有带+号的，则可读可写，不过它们之间还是有区别的
# 读取文件 r 表示只读 read读取的是全部字符
f = open(r'D:/autotest001/test.py', 'r')
content1 = f.read()
print(content1)
f.close()

# readlines读取全部的行，返回的是list
f = open(r'D:/autotest001/test.py', 'r')
content2 = f.readlines()
print(content2)
f.close()

# readline每次只读取第一行，可以循环获取行
f = open(r'D:/autotest001/test.py', 'r')
content3 = f.readline()
print(content3)
f.close()

# 使用with则不需要close文件
with open(r'D:/autotest001/test.py', 'r') as f:
    con4 = f.readlines()
print(con4)

# 如果文件是ascll则可以直接使用以上方式打开，但是如果文件是二进制文件则需要用rb
with open(r'D:/autotest001/test.py', 'rb') as f:
    con5 = f.read()
print(con5)

# 如果文件是要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
with open(r'D:/autotest001/test.py', 'rb') as f:
    con6 = f.read().decode('gbk')
print(con6)

# 如果每次都这么手动转换编码嫌麻烦，Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读unicode：
import codecs
with codecs.open(r'D:/autotest001/test.py', 'rb') as f:
    con7 = f.read()
    print(con7)

# 写文件同样是使用open但是参数是用w写入文本，wb写入二进制文件
#with open(r'D:/autotest001/test.py', 'r+') as f:
#    f.write('444')
with open(r'D:/autotest001/test.py', 'r+') as f1:
    con8 = f1.read()
    print(con8)
