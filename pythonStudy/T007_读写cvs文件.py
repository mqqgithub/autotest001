import csv
# 读取
with open("test.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)

# 写
with open("test.csv", "w", encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index", "a_name", "b_name"])
    writer.writerows([[0, 'a1', 'b1'], [1, 'a2', 'b2'], [2, 'a3', 'b3']])
# 以上写法会使  每一行的后面会多一行，解决如下
with open("test.csv", "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index", "a_name", "b_name"])
    writer.writerows([[0, 'a1', 'b1'], [1, 'a2', 'b2'], [2, 'a3', 'b3']])

# 如果写入文件是含有中文的就是会出现乱码  导入codecs

import csv
import codecs
data = [
    ("测试1", '软件测试工程师'),
    ("测试2", '软件测试工程师'),
    ("测试3", '软件测试工程师'),
    ("测试4", '软件测试工程师'),
    ("测试5", '软件测试工程师'),
]
f = codecs.open('222.csv', 'w', 'gbk')
writer = csv.writer(f)
for i in data:
    writer.writerow(i)
f.close()


