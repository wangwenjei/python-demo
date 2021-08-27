from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# 创建线程池
"""池子造出来之后 里面会固定存在X个线程  这X个线程不会出现重复创建和销毁的过程 """
pool = ThreadPoolExecutor(5)  # 括号内可以不传数字,不传的话默认会开设当前计算机CPU个数五倍的线程


def task(n):
    print(n)
    time.sleep(2)
    return f'异步提交返回结果:{n}'


"""
提交任务的两种方式:
    同步: 提交任务后原地等待任务的返回结果 期间不做任何操作
    异步: 提交任务后不等待任务的返回结果 继续往下执行
         异步任务的返回结果应该通过回调机制来获取
         回调机制:
            就相当于给每个异步任务绑定了一个触发事件
            一旦该任务有结果立刻触发
"""

# pool.submit(task, 1)  # 朝池子中添加任务  submit是异步提交
# print('主')
t_list = []
for i in range(20):  # 朝池子中提交20个任务
    res = pool.submit(task, i)  # ==> <Future at 0x7fb4a3ef37c0 state=running>
    # print(res.result())  # result() 同步提交
    t_list.append(res)

# 等待线程池中所有的任务执行完毕之后再继续往下执行
pool.shutdown()  # 关闭线程池并等待线程池中所有的线程完毕

for t in t_list:
    print(t.result())

"""
程序由并行变成了串行,
res.result() 拿到的就是异步提交的任务返回的结果
"""
