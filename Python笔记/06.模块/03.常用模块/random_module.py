import random

"""
    打印随机字符

print(random.randint(1, 10))     # 产生 1 到 10 的一个整数型随机数

print(random.random())      # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1, 5.4))   # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数

print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
print(random.choice(['a', 'b', 'c', 1, 2, 3]))  随机返回列表中的一个元素

print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数

"""


def make_code(size: int = 4) -> str:
    # 打印随机字符串
    res = ''
    for i in range(size):
        s1 = chr(random.randint(65, 90))
        s2 = str(random.randint(0, 9))
        res += random.choice([s1, s2])
    return res


print(make_code(6))
