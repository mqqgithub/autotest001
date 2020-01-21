# https://www.cnblogs.com/jassin-du/p/7921296.html
"""
from multiprocessing import Process
import os


def add(name):
    print("child process %s,%s" % (name, os.getpid()))


if __name__ == "__main__":
    print("parent process %s" % (os.getpid()))
    print("创建进程实例-子进程")
    # args是一个元祖，传参数值给add
    p = Process(target=add, args=('test1',))
    print("子进程启动")
    p.start()
    print("join子进程执行，等待这个进程结束，主进程才结束，通常用于进程间的同步")
    p.join()
    # 获取当前进程的名字
    # multiprocessing.current_process()
    # 判断这个进程实例，是否还在运行
    # p.is_alive()
    # 不管这个是否在运行，强制杀掉
    # p.terminate()
    # 默认值False，主进程
    # p.daemon = True
"""
"""进程池:进程之间不能通行，数据不能共享
from multiprocessing import Pool
import os
import time


def task(name):
    print("子进程 %s， 执行task %s" % (os.getpid(), name))
    time.sleep(1)


if __name__ == "__main__":
    print("父进程 %s " % os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task, args=(i,))
    print("等待所有子进程结束")
    p.close()
    p.join()
    print("所有子进程结束")
"""
"""queue队列，创建一个子进程向队列中写消息，另一个进程对消息, 队列中的数据是共享的"""
from multiprocessing import Process
from multiprocessing import Queue
import time


def write_task(queue):
    print("队列中写消息")
    if not queue.full():
        for i in range(500):
            msg = "mews" + str(i)
            queue.put(msg)
            print("写入消息%s" % msg)

def read_task(queue):
    print("队列中读消息")
    if not queue.empty():
        for i in range(500):
            news = queue.get(True,2)
            print("读取 %s" % news)


if __name__ == "__main__":
    print("主进程开始")
    print("创建一个队列")
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("主进程结束")