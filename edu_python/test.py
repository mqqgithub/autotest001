def yyy(x, n):
    if n == 0:
        return 1
    else:
        return x*yyy(x, n-1)

print(yyy(3, 5))