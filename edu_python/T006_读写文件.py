# open函数最常用的使用方法如下：文件句柄 = open('文件路径', '模式'，编码方式)。windows 默认GBK
# r    以只读方式打开文件。这是默认模式。文件必须存在，不存在抛出错误
# rb   以二进制格式打开一个文件用于只读。
# r+   打开一个文件用于读写。文件指针将会放在文件的开头。读完就追加。
# w    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+   打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+   打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# 注：后面有带b的方式，不需要考虑编码方式。有带+号的，则可读可写，不过它们之间还是有区别的
# 读取文件 r 表示只读 read读取的是全部字符
'''
f = open(r'D:/autotest001/test.py', 'r')
print(type(f))
content1 = f.read()
print(type(content1))
print("************")
print(content1)
print("************读取文件末尾会多出的空行，指针对到这一行")
print(content1.rstrip())
print("************")
f.close()
'''
'''
# 这样子并没有用readlines() 而是用了循环这样子,但是文本不能拿到循环体外使用

f = open(r'D:/autotest001/test.py', 'r', encoding='utf-8')
for lines in f:
    print(lines)

print(lines)
f.close()
'''



# readlines读取全部的行，返回的是list  每行末尾加\n换行

f = open(r'D:/autotest001/test.py', 'r', encoding='utf-8')
content2 = f.readlines()
print(content2)
f.close()


# readline每次只读取第一行，可以循环获取行
'''
f = open(r'D:/autotest001/test.py', 'r')
content3 = f.readline()
print(content3)
f.close()
'''

# 使用with则不需要close文件
'''
with open(r'D:/autotest001/test.py', 'r') as f:
    con4 = f.readlines()
print(con4)
'''

# 如果文件是ascll则可以直接使用以上方式打开，但是如果文件是二进制文件则需要用rb
'''
with open(r'D:/autotest001/test.py', 'rb') as f:
    con5 = f.read()
print(con5)
'''

# 如果文件是要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
'''
with open(r'D:/autotest001/test.py', 'rb') as f1:
    con6 = f1.read().decode('gbk')
print(con6)
'''

# 如果每次都这么手动转换编码嫌麻烦，Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读unicode：
'''
import codecs
with codecs.open(r'D:/autotest001/test.py', 'rb') as f:
    con7 = f.read()
    print(con7)
    '''

# 写文件同样是使用open但是参数是用w写入文本，wb写入二进制文件
#with open(r'D:/autotest001/test.py', 'r+') as f:
#    f.write('444')
'''
with open(r'D:/autotest001/test.py', 'r+') as f1:
    con8 = f1.read()
    print(con8)
'''
'''
句柄是WONDOWS用来标识被应用程序所建立或使用的对象的唯一整数，
WINDOWS使用各种各样的句柄标识诸如应用程序实例，窗口，控制，位图，GDI对象等等
句柄是一种指向指针的指针
指针是一种内存地址。应用程序启动后，组成这个程序的各对象是住留在内存的
句柄地址(稳定)→记载着对象在内存中的地址————→对象在内存中的地址(不稳定)→实际对象
------------------------
文件的读写过程：
磁盘--》文件缓冲区--》应用程序内存
文本文件是基于字符编码的文件，常见的编码有ASCII编码，UNICODE编码等等。
二进制文件是基于值编码的文件，你可以根据具体应用，指定某个值是什么意思（这样一个过程，可以看作是自定义编码。
就拿它举例子吧，其头部是较为固定长度的文件头信息，前2字节用来记录文件为BMP格式，接下来的8个字节用来记录文件长度，
再接下来的4字节用来记录bmp文件头的长度。


'''
