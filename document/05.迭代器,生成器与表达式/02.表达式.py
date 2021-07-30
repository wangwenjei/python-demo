"""
三元表达式:
    语法格式: 条件成立时返回的值  if  条件  else  条件不成立时返回的值
"""


def func1(x, y):
    res = f'x大于y,x的值为 [{x}]' if x > y else f'x小于y,y的值为 [{y}]'
    return res


print(func1(1, 2))  # ==> x小于y,y的值为 [2]

"""
列表表达式:
    语法格式:  [条件为真输入的值  for i in l if True]

for 循环每次为真时把值添加到新列表,
判断条件可自定义,
不接if判断则表示永远为真
"""

l = ['www_dsb', 'xxx_dsb', 'wwj']
new_l = [name for name in l if name.endswith('dsb')]
print(new_l)  # ==> ['www_dsb', 'xxx_dsb']

"""
字典生成式:
    语法格式:  {key:value for key,value in l if True}
    
for 循环每次为真时将列表中的值解压赋值到 key value 并将值 key:value 添加到新字典中
判断条件可自定义,
不接if判断则表示永远为真

"""

l = [('name', 'wwj', 1), ('age', 18, 1), ('gender', 'man', 2)]
d = {k: v for k, v, i in l if not i == 2}
print(d)  # {'name': 'wwj', 'age': 18}

"""
集合生成式:
    语法格式: [i for i in d if True]

当条件为真时将结合的key 添加到新列表中
"""

d = {'name': 'wwj', 'age': 18, 'gender': 'man'}
l = [i for i in d if not i == 'age']
print(l)  # ==> ['name', 'gender']

"""
生成器表达式

"""
g = (i for i in range(0, 5) if i > 2)

print(next(g))  # ==> 3
print(next(g))  # ==> 4
# print(next(g))  # ==> StopIteration

# 统计一个文件内有多少字符
with open(r'./01.迭代器与生成器.py', mode='rt', encoding='utf-8') as f:
    # 方法一:
    # res = 0
    # for line in f:
    #     res += len(line)

    # 方法二: 当文件行数过大时,会导致集合内元素过多,在sum求和是影响效率
    # res = sum([len(line) for line in f])

    # 方法三: 效率最高
    res = sum((len(line) for line in f))
    print(res)
