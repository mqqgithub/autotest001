import time
def timer(func):  # func = index
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'此函数的执行效率为{end_time-start_time}')
    return inner

index = timer(index)

f()