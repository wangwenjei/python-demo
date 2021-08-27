from multiprocessing import Process
import time


def task():
    print('子进程正常活着')
    time.sleep(5)
    print('子进程正常死亡')


if __name__ == '__main__':
    p = Process(target=task)
    p.daemon = True  # 将进程p设置为守护进程, 这一句一定要放在start方法上面才有效否则会直接报错
    p.start()
    time.sleep(1)
    print('主进程正常死亡')

"""
  只要主进程一结束,子进程随即结束
子进程正常活着
主进程正常死亡
"""
