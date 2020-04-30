# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;
'''
num = 0
i = 0
while i < 10:
    num += i
    i += 1
print(num)
'''


def add(n):
    i = 0
    num = 0
    while i < n:
        num += i
        i += 1
    print(num)
add(11)


name = "吴彦祖"
print(name[:-1])
for i in name:
    i_by = bytes(i, encoding="utf-8")
    for i_bin in i_by:
        i_b = bin(i_bin)
        print(i_b)

#res='{} {} {}'.format('egon',18,'male')
res='{1} {0} {1}'.format('egon',18,'male')
#res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
print(res)