"""
# 计算密集型
"""
# from multiprocessing import Process
# from threading import Thread
# import os, time
#
#
# def work():
#     res = 0
#     for i in range(100000000):
#         res *= i
#
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())
#     start_time = time.time()
#
#     for i in range(4):
#         # 多进程
#         # p = Process(target=work)  # ==> 10.460120916366577
#         # p.start()
#         # l.append(p)
#
#         # 多线程
#         t = Thread(target=work)  # ==> 17.198389053344727
#         t.start()
#         l.append(t)
#
#     for p in l:
#         p.join()
#
#     print(time.time() - start_time)


"""
# IO密集型
"""
from multiprocessing import Process
from threading import Thread
import os, time


def work():
    time.sleep(2)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start_time = time.time()
    for i in range(400):
        # 多进程
        # p = Process(target=work)  # ==> 50.56896710395813
        # p.start()
        # l.append(p)

        # 多线程
        t = Thread(target=work)  # ==> 2.0684468746185303
        t.start()
        l.append(t)

    for p in l:
        p.join()

    print(time.time() - start_time)
