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

