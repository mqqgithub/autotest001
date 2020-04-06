import threading
from time import ctime, sleep
import time


def music():
    for i in range(10):
        print('listening to music{}'.format(ctime()))
        sleep(1)

def movie():
    for i in range(10):
        print('look at movie{}'.format(ctime()))
        sleep(2)

threads = []
thread1 = threading.Thread(target=music, name='music')
threads.append(thread1)
thread2 = threading.Thread(target=movie, name='movie')
threads.append(thread2)

if __name__ == '__main__':

    print('starting...{}'.format(ctime()))
    t1 = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    t2 = time.time()
    print('ending...{}'.format(ctime()))
    print('all time=%.8f' % (t2-t1))

'''
1、创建线程组
2、指定线程要执行的函数target=func
3、把线程加到线程组中append（）
4、设置守护线程setDaemon（），等到子线程都结束，主线程才结束
https://www.cnblogs.com/JackLi07/p/9232005.html
'''