# 第一种方法, 常用这种方法开启多进程

from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is over' % name)


if __name__ == '__main__':
    # 1.创建一个对象
    p = Process(target=task, args=('jason',))
    # print(p)  # ==> <Process name='Process-1' parent=84282 initial>
    # 2.开启进程
    p.start()  # 告诉操作系统创建一个进程
    p.join()  # 等待子进程p运行结束之后再继续往后执行
    print('主')

"""
Windows操作系统下,创建进程一定要在admin内创建
因为Windows下创建进程类似与模块导入的方式
会从上往下依次执行代码

linux中则是直接将代码完整的拷贝一份

"""

# 第二种方式, 类的继承
# from multiprocessing import Process
# import time
#
#
# class MyProcess(Process):
#     def run(self) -> None:  # 函数名必须要叫 run
#         print('hello world')
#         time.sleep(3)
#         print('game over')
#
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()
#     print('主')


