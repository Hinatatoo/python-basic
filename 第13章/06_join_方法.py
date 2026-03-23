import os
import time
from multiprocessing import Process


def speak():
    for index in range(10):
        print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)


def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    p2.start()

    p1.terminate()
    p1.join()
    print(p1.is_alive())
    print('我是主进程中的【最后一行】打印')
