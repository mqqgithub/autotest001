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
print("a=", a, "    id(a)=", id(a), "id(a[4])", id(a[4]), "id(a[5])=", id(a[5]), "id(a[5][0]", id(a[5][0]))
print("b=", b, "    id(b)=", id(b), "id(a[4])", id(a[4]), "id(b[5])=", id(b[5]), "id(a[5][0]", id(a[5][0]))
print("c=", c, "    id(c)=", id(c), "id(a[4])", id(a[4]), "id(c[5])=", id(c[5]), "id(a[5][0]", id(a[5][0]))
print("d=", d, "    id(d)=", id(d), "id(a[4])", id(a[4]), "id(d[5])=", id(d[5]), "id(a[5][0]", id(a[5][0]))
print("*"*70)

a.append(6)  # 修改对象a
a[5].append('c')  # 修改对象a中的['a','b']数组对象
print("a=",a,"    id(a)=",id(a),"id(a[5])=",id(a[5]))
print("b=",b,"    id(b)=",id(b),"id(b[5])=",id(b[5]))
print("c=",c,"    id(c)=",id(c),"id(c[5])=",id(c[5]))
print("d=",d,"    id(d)=",id(d),"id(d[5])=",id(d[5]))

# 浅copy，列表重新开辟内存地址，列表中的值还是原来的不变
# 深copy，列表重新开辟内存地址，列表中不可变对象地址还是用原来的，可变对象重新开辟内存地址
