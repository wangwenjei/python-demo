from multiprocessing import Process, Queue, JoinableQueue, set_start_method
import time
import random


def producer(name, food, q):
    for i in range(1, 6):
        data = '%s 生成了 %s 个 %s' % (name, i, food)

        # 模拟延迟
        time.sleep(random.randint(1, 3))

        print(data)
        # 将数据放入队列中
        q.put(data)


def consumer(name, q):
    while True:
        food = q.get()
        if food is None: break
        time.sleep(random.randint(1, 3))
        print('%s 吃个 %s' % (name, food))
        q.task_done()  # 告诉队列你已经从里面取出了一个数据,并且处理完毕了


if __name__ == '__main__':
    set_start_method('fork')

    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=('厨师Lucy', '包子', q))
    p2 = Process(target=producer, args=('厨师Tom', '烧麦', q))

    c1 = Process(target=consumer, args=('客人user1', q))
    c2 = Process(target=consumer, args=('客人user2', q))

    p1.start()
    p2.start()

    # 将消费者设置为守护进程
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    # 等待生产者生产完毕之后,往队列中添加特定的结束符号
    # q.put(None)  # 肯定在所有生产者生产的数据的末尾
    # q.put(None)

    # 只要q.join()执行完毕 说明消费者已经处理完数据了 消费者就没有存在的必要了 (用到了守护进程知识点)
    q.join()  # 等待队列中所有的数据被取完,在执行往下的代码

    """
    JoinableQueue() 每当你往队列中存入数据的时候,内部会有一个计数器 +1 
    每当你调用 task_done() 的时候,计数器 -1
    q.join() 当计数器为0的时候 才往后运行
    """
