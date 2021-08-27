# from threading import Thread
# import time

""""
主线程运行结束后不会立即结束,会等待所有其他非守护线程结束后才会结束
    因为主线程的结束意味着所在的进程结束
"""

# def task(name):
#     print('%s is running' % name)
#     time.sleep(3)
#     print('%s is over' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('Lucy',))
#     t.daemon = True
#     t.start()
#     print('主')

""" ===>
Lucy is running
主
"""

from threading import Thread
import time


def foo():
    print(123)
    time.sleep(1)
    print('end123')


def func():
    print(456)
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=func)
    t1.daemon = True
    t1.start()
    t2.start()

    print('主......')

""" ===>
123
456
主......
end123
end456
"""