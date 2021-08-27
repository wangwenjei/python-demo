from multiprocessing import Queue

"""
q.full()
q.empty()
q.get_nowait()
这三种方法在多进程下是不精确的
 

"""
# 创建一个队列
q = Queue(5)  # 括号内可以传数字,表示生产队列最大可以同时存放的数据量

# 往队列中存数据
q.put(111)
q.put(222)
q.put(333)
print(q.full())  # ==> False  判断当前队列是否满了
q.put(444)
q.put(555)
# q.put(666)  # 当队列数据放满了之后, 如果还有数据要存入程序会堵塞, 直到有位置让出来, 但不会报错

# 从队列中取数据
v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
print(q.empty())  # ==> True  判断当前队列是否空了
# v6 = q.get()  # 队列中如果已经没有数据的话, get方法会原地堵塞
# v6 = q.get_nowait()   # 没有数据直接报错 _queue.Empty
# v6 = q.get(timeout=3)  # 没有数据后原地等待3秒再报错  _queue.Empty

try:
    v6 = q.get(timeout=3)
    print(v6)


except Exception as e:
    print('队列被取完了')

# print(v1, v2, v3, v4, v5,)  # ===> 111 222 333 444 555
