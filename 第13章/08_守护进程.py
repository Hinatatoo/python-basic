import os
import time
from multiprocessing import Process
from os import times_result


def monitor():
    while True:
        try:
            with open('log.txt', 'r', encoding='utf-8') as file:
                lines = sum(1 for _ in file)
        except FileNotFoundError:
            lines = 0
        print(f'我是守护进程({os.getpid()}),log.txt共有{lines}行')
        time.sleep(1)


def test():
    for index in range(30):
        print(f'我是test{index}({os.getpid()})')
        time.sleep(1)


if __name__ == '__main__':
    print(f'我是主进程({os.getpid()})中的【第一行】代码')

    p1 = Process(target=monitor, daemon=True)
    p2 = Process(target=test)

    p1.start()
    p2.start()

    with open('log.txt', 'a', encoding='utf-8') as file:
        for index in range(10):
            file.write(f'good{index}\n')
            file.flush()
            time.sleep(1)

    print(f'我是主进程({os.getpid()})中的【最后一行】代码')
