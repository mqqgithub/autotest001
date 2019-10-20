# while 当条件为TRUE，循环会一直执行下去
n = 0
su = 0
counter = 1
while counter <= n:
    su = su + counter
    counter += 1
print(su)

# for in
languages = ["C", "C++", "Perl", "Python"]
for i in languages:
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 9, 2):
    print(i)

# 查找200以内所有的质数
# 分析质数除了1和本身，没有别的可以整除的约束num%i==0
loop = 0
for num in range(1, 200):
    count = 0
    for i in range(2, int(num/2)+1):
        loop += 1
        if num % i == 0:
            count += 1
    if count == 0:
        print(f"{num}是质数")
print(loop)
# 查看代码运行了多少次loop ，想想怎能优化
# 1和本身是不用判断的 所以可以从2和num-1循环 如果可以被平方根整除
