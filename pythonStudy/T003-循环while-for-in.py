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

