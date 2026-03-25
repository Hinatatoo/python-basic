import os,time
from threading import get_native_id,Thread,RLock

def speak(lock):
    for index in range(5):
        with lock:
            print(f'我在说话{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
        time.sleep(1)

def study(lock):
    for index in range(5):
        with lock:
            print(f'我在学习{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
        time.sleep(1)

if __name__=='__main__':
    print(f'-------start------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
    lock=RLock()

    t1=Thread(target=speak,args=(lock,))
    t2=Thread(target=study,args=(lock,))

    t1.start()
    t2.start()
    print('-------end-------')
