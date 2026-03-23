import os, time
from multiprocessing import Process, current_process

print(100, __name__, os.getpid())


def speak():
    for index in range(10):
        print(f'--{current_process().name}--我在说话{index},进程pid是：{os.getpid()},我的父进程pid是：{os.getppid()}')
        time.sleep(1)


def study():
    for index in range(10):
        print(f'--{current_process().name}--我在学习{index},进程pid是：{os.getpid()},我的父进程pid是：{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    print('我是主进程中的第一行打印')

    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    p2.start()

    print('我是主进程中的最后一行打印')
