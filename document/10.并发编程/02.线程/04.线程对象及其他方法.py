from threading import Thread, active_count, current_thread
import os, time


def task(n):
    # print('hello', os.getpid())  # ==> hello 99694  验证子线程与主进程是同一个PID号
    print('hello', current_thread().name)  # ==> hello Thread-1  获取当前线程的名字
    time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=task, args=(1,))
    t1 = Thread(target=task, args=(3,))
    t.start()
    t1.start()

    t.join()
    print('主', active_count())  # ==> 主 1  统计当前线程数
    # print('主', os.getpid())  # ==> 主 99694
    # print('主', current_thread().name)  # ==> 主 MainThread

