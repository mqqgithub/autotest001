import os, re
path1 = os.path.join(os.getcwd(), 'T000.py')
# 文件时utf-8的的二进制文件，读取的时候需要带上编码格式
# 也可以rb模式读取文件，读取的文件b开始的字符串，不需要带上编码格式
# 读取的文件每行的结尾都带上\n
# with open(path, 'r', encoding='utf-8') as f:
#     lines = []
#     for line in f:   # 每次读取一行，读完就释放空间，读取下一行
#         lines.append(line)
# print(lines)


def read_size(path, size):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            line = f.read(size)  # size代表字符个数，1=1个汉字=1个字母=1个数字=1个换行符\n,rb方式size代表byte
            # 当文件没有更多内容时，read 调用将会返回空字符串 ''
            if not line:
                break
            yield line


for line in read_size(path1, 8*1024):
    list1 = []
    for l in re.split(r"(?:\s)", line):    # 按照所有空格；，|切分成list
        list1.append(l)
    print(list1)

# [x for x in s.split(',') if x]  三种去掉空字符的方式
# # list(filter(None,s.split(',')))
# # re.findall('[a-z0-9]+',s)