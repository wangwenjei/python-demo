from multiprocessing import Queue, Process, set_start_method


def producer(q):
    q.put('队列001')


def consumer(q):
    print(q.get())


# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=producer, args=(q,))
#     p.start()
#     print(q.get())  # ==>  队列001   验证 主进程跟子进程借助队列通信

if __name__ == '__main__':
    set_start_method('fork')

    q = Queue()
    p = Process(target=producer, args=(q,))
    p1 = Process(target=consumer, args=(q,))
    p.start()
    p1.start()  # ==>  队列001  验证 子进程 跟 子进程 借助队列通信

