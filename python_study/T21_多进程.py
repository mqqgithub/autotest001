# https://www.cnblogs.com/jassin-du/p/7921296.html

from multiprocessing import Process
import os


def add(name):
    print("child process %s,%s" % (name, os.getpid()))


if __name__ == "__main__":
    print("parent process %s" % (os.getpid()))
    print("创建子进程实例")
    # args是一个元祖，传参数值给add
    p = Process(target=add, args=('test1',))
    print("子进程启动")
    p.start()
    print("join 等待这个进程结束，主进程才结束，通常用于进程间的同步")
    p.join()
    # 获取当前进程的名字
    # multiprocessing.current_process()
    # 判断这个进程实例，是否还在运行
    # p.is_alive()
    # 不管这个是否在运行，强制杀掉
    # p.terminate()
    # 默认值False，主进程
    # p.daemon = True
