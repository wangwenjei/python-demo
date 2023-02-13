from threading import Thread
import time


def task(name):
    print('%s is running' % name)
    time.sleep(1)
    print('%s is over' % name)





# 开启线程不是必须要在__main__下执行代码, 直接写就可以了
# 但是习惯还是写在__main__下

t = Thread(target=task, args=('Tom',))
t.start()
print('主')
"""
===>
Tom is running
主
Tom is over
"""


# 第二种方式, 类的继承

# from threading import Thread
# import time
#
#
# class MyThread(Thread):
#     def __init__(self, name):
#         # 重写了别人的方法又不知别人的方法里面有啥,就需要重新调用父类的方法
#         super().__init__()
#         self.name = name
#
#     def run(self) -> None:  # 这里函数名必须要叫 run
#         print('%s is running' % self.name)
#         time.sleep(1)
#         print('%s is over' % self.name)
#
#
# if __name__ == '__main__':
#     t = MyThread('Lucy')
#     t.start()
#     print('主')

"""
===>
Lucy is running
主
Lucy is over
"""