#   n!
# 方法1
n = 10
m = 1
for i in range(1,n+1):
    m *= i
print(m)


# 方法二
def mult(num):
    if num == 1:
        return 1
    elif num > 1:
        return num*mult(num-1)

print(mult(10))


#  方法三
from functools import reduce
c = reduce(lambda x, y: x*y, range(1, 11))
print(c)