from concurrent.futures import ThreadPoolExecutor
import time

# 创建线程
pool = ThreadPoolExecutor(5)


def task(n):
    print(n)
    time.sleep(2)
    return n


# 回调函数
def call_back(n):
    print(f'异步提交返回结果:{n.result()}')


if __name__ == '__main__':
    for i in range(20):
        res = pool.submit(task, i).add_done_callback(call_back)

"""
0
1
2
3
4
异步提交返回结果:1
5
异步提交返回结果:0
6
异步提交返回结果:3异步提交返回结果:2
7
异步提交返回结果:4
8
9
异步提交返回结果:5
10
异步提交返回结果:6
异步提交返回结果:7
11
12
异步提交返回结果:8
13
异步提交返回结果:9
14
异步提交返回结果:10
异步提交返回结果:11
15
16
异步提交返回结果:12
17
异步提交返回结果:13
18
异步提交返回结果:14
19
异步提交返回结果:16
异步提交返回结果:15
异步提交返回结果:17
异步提交返回结果:18
异步提交返回结果:19




"""