# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明

import copy
a = [1, 2, 3, 4, 5, ['a', 'b']]
# 原始对象
b=a  # 赋值，传对象的引用  可以认为a就是b
c=copy.copy(a)  # 对象拷贝，浅拷贝，复制a的值并开辟了新的内存地址， 但是a[5]和c[5]确实同一个没变，只copy了第一次
d=copy.deepcopy(a)  # 对象拷贝，深拷贝，copy了2层，和copy的值没有任何关系了，是全新的
print("a=", a, "    id(a)=", id(a), "id(a[5])=", id(a[5]))
print("b=", b, "    id(b)=", id(b), "id(b[5])=", id(b[5]))
print("c=", c, "    id(c)=", id(c), "id(c[5])=", id(c[5]))
print("d=", d, "    id(d)=", id(d), "id(d[5])=", id(d[5]))
print("*"*70)

a.append(6)  # 修改对象a
a[5].append('c')  # 修改对象a中的['a','b']数组对象
print("a=",a,"    id(a)=",id(a),"id(a[5])=",id(a[5]))
print("b=",b,"    id(b)=",id(b),"id(b[5])=",id(b[5]))
print("c=",c,"    id(c)=",id(c),"id(c[5])=",id(c[5]))
print("d=",d,"    id(d)=",id(d),"id(d[5])=",id(d[5]))

# 可变对象，重新赋值，值改变，但是内存地址不变
# 不可变对象，重新赋值，重新指向内存地址，是全新的
