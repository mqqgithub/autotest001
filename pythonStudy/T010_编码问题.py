# 参考此文章https://www.cnblogs.com/vipchenwei/p/6993788.html
'''
内存中使用的编码是unicode，用空间换时间（程序都需要加载到内存才能运行，因而内存应该是尽可能的保证快）；
硬盘中或者网络传输用utf-8，网络I/O延迟或磁盘I/O延迟要远大与utf-8的转换延迟，而且I/O应该是尽可能地节省带宽，
保证数据传输的稳定性。

不管是哪种类型的文件，只要记住一点：文件以什么编码保存的，就以什么编码方式打开.

如果不在python文件指定头信息＃-*-coding:utf-8-*-,那就使用默认的python2中默认使用ascii，python3中默认使用utf-8

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器
如果服务端encode的编码格式是utf-8， 客户端内存中收到的也是utf-8编码的二进制

Unicode是数据解码后的结果，所以如果数据已经是Unicode格式，则只能使用encode，如果是其他格式只能使用decode

#1.win系统默认是gbk编码的，所以桌面生成的TXT之类的都是gbk编码的。
#2.出现乱码正常都是原文件的编码方式和打开指定的编码不一致所致
'''
print(id("hello"))
x = 'hello' # x在内存是unicode 编码
print(id(x))

y = 'hello'.encode('utf-8') # y在内存是utf-8编码
print(y)
print(id(y))
print('#################################')
# 分别验证在pycharm中和cmd中下述的打印结果
s = u'林' # 当程序执行时，'林'会被以unicode形式保存新的内存空间中
print('__'+repr(s))
# s指向的是unicode，因而可以编码成任意格式，都不会报encode错误
s1 = s.encode('utf-8')
s2 = s.encode('gbk')
print(s1) # 打印正常否？
print(s2) # 打印正常否

print(repr(s)) # u'\u6797'
print(repr(s1)) # '\xe6\x9e\x97' 编码一个汉字utf-8用3Bytes
print(repr(s2)) # '\xc1\xd6' 编码一个汉字gbk用2Bytes

print(type(s)) # <type 'unicode'>
print(type(s1)) # <type 'str'>
print(type(s2)) # <type 'str'>
