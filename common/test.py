def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

print(fab(6))
f = fab(5)
for i in f:
    print(id(f))
    print(i)