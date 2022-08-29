from threading import Thread, Lock
import time

money = 100
mutex = Lock()


def task():
    global money

    # 加锁
    mutex.acquire()
    tmp = money
    time.sleep(0.01)
    money = tmp - 1
    # 释放锁
    mutex.release()

    # 利用上下文管理 添加锁,释放锁
    # with mutex:
    #     tmp = money
    #     time.sleep(0.01)
    #     money = tmp - 1


if __name__ == '__main__':
    t_list = []
    for i in range(100):
        t = Thread(target=task)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print(money)


"""
100个线程起起来之后 先去抢GIL
当我进入IO GIL自动释放 但是我手上还有一个自己的互斥锁
其他线程虽然抢到了GIL但是抢不到互斥锁 
最终GIL还是回到你的手上 你去操作数据
"""