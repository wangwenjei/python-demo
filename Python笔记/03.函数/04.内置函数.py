# map 映射
l = [1, 2, 3, 4]
res = map(lambda x: x ** 2, l)
print(list(res))  # ==> [1, 4, 9, 16]

# zip 拉链函数,将v1 中的值与v2 中的值做一一对应 多余的舍弃
v1 = 'hello'
v2 = [11, 22, 33, 44, 55, 66]
res = zip(v1, v2)
print(list(res))  # ==> [('h', 11), ('e', 22), ('l', 33), ('l', 44), ('o', 55)]

# reduce 多个进,一个出
from functools import reduce
l = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x + y, l, 100)
print(res)  # ==>  115

# filter 过滤
l = [1, 2, 3, 4, 5, 6, 7]
res = filter(lambda x: x > 3, l)
print(list(res))  # ===> [4, 5, 6, 7]

# 求绝对值
print(abs(-1))  # ==> 1

# 全部为True 返回True
print(all([1, 'aaa', True, None]))  # ==> False
# 只要有一个为True 返回True
print(any([1, 'aaa', None, True]))  # ==> True

# 将数字转为对应的字符
print(chr(65))  # ==> A
# 将字符转为对应的数字
print(ord('A'))  # ==> 65

# 将计算后的商和余数放在一个元组内
print(divmod(10, 3))  # (3, 1)

# 查看对象都有哪些属性
print(dir(object))

# 类型判断, 推荐使用isinstance
print(isinstance([], list))  # ==> True
print(type([]) is list)  # ==> True

# 要导入的模块是从配置文件中读取的,将会是str类型的,可以用 __import__ 来导入模块
# import 'time'  #  import 不可以导入str 类型
time1 = __import__('time')
print(time1.time())  # ==> 1627981445.093905
