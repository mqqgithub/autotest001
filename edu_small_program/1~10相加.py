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

print('*'*22)
def add(n):
    i = 0
    num = 0
    while i <= n:
        num += i
        print(num)
        i += 1
        print(i)
    print(num)
add(10)
print('*'*22)

print(sum({i for i in range(11)}))


name = "吴彦祖"
print(name[:-1])
for i in name:
    i_by = bytes(i, encoding="utf-8")
    for i_bin in i_by:
        i_b = bin(i_bin)
        print(i_b)

# res='{} {} {}'.format('egon',18,'male')
res = '{1} {0} {1}'.format('egon', 18, 'male')
# res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
print(res)

# 列表推导式
print(sum([1, 2, 3]))
print(sum({i*2 for i in range(0, 11)}))
