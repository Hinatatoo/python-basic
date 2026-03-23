import os, time
from multiprocessing import Process, Lock


def speak(lock):
    for index in range(10):
        lock.acquire()
        print('好好', end='')
        print('学习', end='')
        print('天天', end='')
        print('向上')
        lock.release()
        time.sleep(1)


def study(lock):
    for index in range(10):
        with lock:
            print('A', end='')
            print('B', end='')
            print('C', end='')
            print('D')
        time.sleep(1)


if __name__ == '__main__':
    print('我是主进程中的第一行打印')
    lock = Lock()
    p1 = Process(target=speak, args=(lock,))
    p2 = Process(target=study, args=(lock,))
    p1.start()
    p2.start()
    print('我是主进程中的最后一行打印')
