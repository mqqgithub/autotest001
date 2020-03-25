import random
# 随机邮箱
user_name = ''.join(random.sample('123456789abcdef', 5)) + "@163.com"
print(user_name)

