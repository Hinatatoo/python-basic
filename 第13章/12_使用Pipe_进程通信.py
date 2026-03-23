import time
from multiprocessing import Process, Pipe


def test1(con):
    time.sleep(2)
    con.send(1000)
    print('test1发送了1000')


def test2(con):
    data = con.recv()
    print(f'test2接收了{data}')


if __name__ == '__main__':
    con1, con2 = Pipe(duplex=False)
    p1 = Process(target=test1, args=(con2,))
    p2 = Process(target=test2, args=(con1,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
