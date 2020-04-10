import random
import string
# 随机邮箱
user_name = ''.join(random.sample('123456789abcdef', 5)) + "@163.com"
print(user_name)
# 生成一个随机数0-1
print(random.random())
# 生成一到10的随机数
print(random.randint(1, 10))

print(random.uniform(1.0, 10.0))
# 随机一个字符
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))
# 随机一个偶数
print(random.randrange(0, 100, 2))
# 从中生成5个字符
print(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
# 生成字符串
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)
# 组成新的字符串
s = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
print(s)