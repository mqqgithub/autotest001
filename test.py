l1 = [1, 2, 3, 4, ['alex']]
l2 = l1[::]
l1[-1].append(666)
print(l2)
print(id(l1))
print(id(l2))
print(id(l1[0]),id(l1[-1]))
print(id(l2[0]),id(l2[-1]))