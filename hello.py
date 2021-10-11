import random

# print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
# print(random.random())  # 产生 0 到 1 之间的随机浮点数
# print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
# print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
# print(random.choice(['a', 'b', 'c', 1, 2, 3]))
import readline

a1 = {1: 'a', 2: 'b', 3: 'c'}
print(a1.items())  # ==> dict_items([(1, 'a'), (2, 'b'), (3, 'c')])

for key, value in a1.items():
    print(key, value)
# ==>
# 1 a
# 2 b
# 3 c

for i in a1.items():
    print(i)

a = 'hello world'
print(a.replace('ll', 'LL'))

print('abcdabcd'.index('c', 3))

course_list_msg = {'QH': ['Python', 'Java', 'GO'], 'BD': ['LINUX', 'Python']}
a = list(course_list_msg.keys())
print(a, type(a))
print(a)  # ==> ['QH', 'BD']

c = [1, 2, 3]
print(list(c))


with open('document/02.文件操作/file/write.txt', mode='rt', encoding='utf-8') as f:
    res = f.readlines()
    old_num=''
    for i in range(len(res)):
        old_num += res[i].strip('\n') + "+"
    print(old_num.strip('+'))
