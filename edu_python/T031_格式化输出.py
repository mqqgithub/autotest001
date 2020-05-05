

print('姓名：%s，年龄：%d' %('jackk', 18))
print('姓名：{}，年龄：{}'.format('jackk', 18))

name = 'jack'
age = 19
print(f'姓名:{name}，年龄：{age}')
print(f'姓名:{"jack"}，年龄：{10}')
print(f'姓名:{name.upper()}，年龄：{age+2}')

li = [1, 'a']
print(f"{li[0]}!={li[1]}")
print(f"{li*2}")


def sum(a ,b):
    return a+b

print(f'求和：{sum(1,2)}')
