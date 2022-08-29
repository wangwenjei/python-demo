from multiprocessing import Process, current_process
import time
import os

"""
current_process().pid  查看当前进程的进程号

os.getpid()   查看当前进程进程号
os.getppid()  查看当前进程父进程进程号
"""


def task():
    # print('子 PID: %s' % current_process().pid)  # 查看当前进程的进程号
    print('os 子 PID: %s' % os.getpid())  # 查看当前进程的进程号
    print('os 主 PID: %s' % os.getppid())  # 查看当前进程的进程号
    time.sleep(3)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()  # 杀死当前进程  是告诉操作系统杀死当前进程,需要一定的时间间隔而代码的运行速度很快
    time.sleep(0.1)
    print(p.is_alive())  # ==> False  判断当前进程是否存活
    # print('主 PID %s' % current_process().pid)
    print('os 主 PID %s' % os.getpid())
    print('os 主主 PID %s' % os.getppid())
