from multiprocessing import Process
import time


def task(name, n):
    print('%s is running' % name)
    time.sleep(n)
    print('%s is over' % name)


if __name__ == '__main__':
    # p1 = Process(target=task, args=('Json', 1))
    # p2 = Process(target=task, args=('Tom', 2))
    # p3 = Process(target=task, args=('Lucy', 3))
    #
    # start_time = time.time()
    #
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()

    start_time = time.time()
    p_list = []
    for i in range(1, 4):
        p = Process(target=task, args=('子进程%s' % i, i))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('主', time.time() - start_time)

""" ===> 
    Json is running
    Lucy is running
    Tom is running
    Json is over
    Tom is over
    Lucy is over
    主 3.4877960681915283
    
    
===>
    子进程3 is running
    子进程1 is running
    子进程2 is running
    子进程1 is over
    子进程2 is over
    子进程3 is over
    主 3.4455819129943848
"""
