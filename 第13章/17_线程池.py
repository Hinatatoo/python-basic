import os, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id, Thread, RLock

def work(n,lock):
    with lock:
        print(f'work正在执任务{n}......{get_native_id()}')
    if n==1:
        time.sleep(15)
    elif n==2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'任务{n}的结果'

if __name__=='__main__':
    print('-----------start----------')
    executor=ThreadPoolExecutor(3)
    lock=RLock()
    # executor.submit(work,1,lock)
    # executor.submit(work,2,lock)
    # executor.submit(work,3,lock)
    # executor.submit(work,4,lock)
    # executor.submit(work,5,lock)
    # executor.submit(work,6,lock)
    # executor.submit(work,7,lock)

    # futures=[executor.submit(work,index,lock) for index in range(1,8)]
    # result_list=[]
    # def done_func(f):
    #     result_list.append(f.result())

    # for f in as_completed(futures):
    #     result_list.append(f.result())

    # for index in range(1,8):
    #     f=executor.submit(work,index,lock)
    #     f.add_done_callback(done_func)


    # for f in futures:
    #     print(f.result())

    # print(result_list)

    result=executor.map(work,range(1,8),[lock]*7)

    print(list(result))
    executor.shutdown(wait=True)

    print('-----------end----------')
