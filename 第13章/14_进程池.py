import os,time
from concurrent.futures import ProcessPoolExecutor, as_completed


def work(n):
    print(f'work正在执行任务{n}......{os.getpid()}')
    if n==1:
        time.sleep(15)
    elif n==2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'我是任务{n}的结果'

if __name__=='__main__':
    print('---------start-------------')
    # executor=ProcessPoolExecutor(3)

    # executor.submit(work,1)
    # executor.submit(work,2)
    # executor.submit(work,3)
    # executor.submit(work,4)

    # futures=[executor.submit(work,index) for index in range(1,8)]

    # result_list=[]
    # for f in as_completed(futures):
    #     result_list.append(f.result())

    # def done_func(future):
    #     result_list.append(future.result())
    #
    # for index in range(1,8):
    #     f=executor.submit(work,index)
    #     f.add_done_callback(done_func)
    #
    # executor.shutdown(wait=True)

    # print(result_list)

    # for f in futures:
    #     print(f.result())


    with ProcessPoolExecutor(3) as executor:
        results=executor.map(work, range(1,8))
        print(list(results))
        
    print('---------end-------------')