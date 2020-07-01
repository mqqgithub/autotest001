cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
# 根据cars得到如下结构
# info = {'鲁': 2, '黑': 3, '京': 1, '沪': 1}
li = [car[0] for car in cars]
set1 = set(li)
info = {}
for t in set1:
    info[t] = li.count(t)

print(info)