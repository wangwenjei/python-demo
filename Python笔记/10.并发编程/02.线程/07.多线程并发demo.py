import time
from threading import Thread

'''
Thread其他初始化参数：
target:指定任务函数
name:指定线程分组
'''


class MyThread(Thread):

    def run(self):
        for i in range(10):
            time.sleep(1)
            print("请求第{}次".format(self.name, i))


if __name__ == '__main__':
    start_time = time.time()
    for i in range(5):
        t = MyThread(name=f"线程{i+1}")
        t.start()


    time.sleep(10)
    end_time = time.time()

    print(end_time - start_time)
