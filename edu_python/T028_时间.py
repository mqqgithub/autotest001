# 功能描述：
# 开发人员：
# 开发时间：
# 参数说明;
import time

t = time.time()
print(t)

t1 = time.localtime()
print(t1)

t2 = time.ctime()
print(t2)

t3 = time.ctime(t)
print(t3)

t4 = time.strftime("%y_%m_%d_%H_%M_%S")
print("...."+t4)


