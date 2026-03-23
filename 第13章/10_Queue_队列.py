import time
from multiprocessing import Queue, Process

'''
q1=Queue()
q2=Queue(3)

q1.put(100)
q1.put(200)
q1.put(300)

value1=q1.get()
value2=q1.get()
value3=q1.get()
print(value1)
print(value2)
print(value3)

result=q1.full()
print(result)

q2.put(100)
q2.put(200)
q2.put(300)
result=q2.full()
print(result)

# q2.put(100)
# q2.put(100)
# q2.put(100)
# q2.put(400,timeout=4)

# q2.put_nowait(400)
# q2.put(400,block=False)

q2.get()
q2.get()
q2.get()
q2.get()

q2.get(timeout=4)

q2.get_nowait()
q2.get(block=False)

'''


def test(q):
    time.sleep(4)
    result = q.get()
    print('我从队列中取出了一个元素：', result)


if __name__ == '__main__':
    q = Queue(2)
    q.put(100)
    q.put(200)
    print(f'队列是否已满:{q.full()}')
    p1 = Process(target=test, args=(q,))
    p1.start()
    print('即将向已满的队列中添加一个元素........')
    q.put('hello')
    print('目前队列中有的元素是：')
    print(q.get())
    print(q.get())
