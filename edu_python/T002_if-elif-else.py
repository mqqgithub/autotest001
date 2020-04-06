# if

a = 400000000000000000000000000000
b = 2
c = 400000000000000000000000000000
if a == c:
    print('==')
    print(id(a), id(b), id(c))

elif a > c:
    print('>')
else:
    print('<')

a = 'a'
b = 'a'
if a == b:
    print('str引用类型')

s1 = [1, 2]
s2 = [1, 2]
if s1 == s2:
    print('list引用类型')
