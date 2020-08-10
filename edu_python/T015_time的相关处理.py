import time

# 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
t = time.time()
print(t)
# 作用是格式化时间戳为本地的时间
print(time.localtime())
# 格式化时间
print(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime()))
