from multiprocessing import Process, Lock, set_start_method
import json
import time
import random

"""
注意: 
    1. 锁不要轻易的使用,容易造成锁死现象,(一般不会自己写,都是用内部封装好的)
    2. 锁只在处理数据的部分加来保证数据安全(只在争抢数据的环节加锁处理即可)
"""


# 查询余票
def search(i):
    with open(r'data', mode='r', encoding='utf8') as f:
        dic = json.load(f)
    print('用户%s查询余票：%s' % (i, dic.get('ticket_num')))


# 买piao
def buy(i):
    with open(r'data', mode='r', encoding='utf8') as f:
        dic = json.load(f)

    # 模拟网络延迟
    time.sleep(random.randint(1, 3))

    # 买票
    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1
        with open(r'data', mode='w', encoding='utf8') as f:
            json.dump(dic, f)
        print('用户%s买票成功' % i)

    else:
        print('用户%s买票失败,暂无余票' % i)


def run(i, mutex):
    search(i)

    # 为买票环节加锁
    mutex.acquire()

    buy(i)
    # 释放锁
    mutex.release()


if __name__ == '__main__':
    # MAC电脑默认启动进程的方式是fork，而python默认的方式是spawn，所以需要将python启动进程的方式做修改, 否则MAC运行会报  exitcode = _main(fd, parent_sentinel)  错
    set_start_method('fork')

    # 在主进程中生成一把锁 让所有的子进程抢 谁先抢到谁先买票
    mutex = Lock()
    for i in range(1, 11):
        p = Process(target=run, args=(i, mutex))
        p.start()
