#!/bin/python3

metadata = [
    {'name': 'andy', 'age': '16'},
    {'name': 'andy', 'age': '17'},
    {'name': 'andy', 'age': '18'},
    {'name': 'andy', 'age': '19'},
    {'name': 'andy', 'age': '20'},
    {'name': 'andy', 'age': '21'},
    {'name': 'andy', 'age': '22'},

    {'name': 'jack', 'age': '17'},
    {'name': 'jack', 'age': '18'},
    {'name': 'jack', 'age': '19'},
    {'name': 'jack', 'age': '20'},
    {'name': 'jack', 'age': '21'},
    {'name': 'jack', 'age': '22'},

    {'name': 'marry', 'age': '18'},
    {'name': 'marry', 'age': '19'},
    {'name': 'marry', 'age': '20'},
    {'name': 'marry', 'age': '21'},
    {'name': 'marry', 'age': '22'},

    {'name': 'jason', 'age': '19'},
    {'name': 'jason', 'age': '20'},
    {'name': 'jason', 'age': '21'},
    {'name': 'jason', 'age': '22'},

    {'name': 'vivi', 'age': '20'},
    {'name': 'vivi', 'age': '21'},
    {'name': 'vivi', 'age': '22'},

    {'name': 'tom', 'age': '16'},
    {'name': 'tom', 'age': '22'},

    {'name': 'lili', 'age': '22'},
]
# 先根据metadata列表中 name字段排序, 再根据age字段排序
metadata = sorted(metadata, reverse=True, key=lambda i: (i['name'], i['age']))

num = 0  # 元数据下标
o = 0  # 同一类数据临时次数计数
g = 0  # 组数
min_index = 5  # 顺着数

t_max = []

while num < len(metadata):
    # 因数据降序处理过,故每组第一个数据就是改组最大数
    if o == 0:
        str_max = metadata[num].get('age')
        t_max.append({
            'name': metadata[num].get('name'),
            'max_time': str_max,
            'min_time': ''
        })
        g += 1

    """
        1. 比较当前一个值的用户名与下一个值的用户名是否一致,当数组长度与下标数加一相等说明已经比较到最后一个数值,此时跳出循环
        2. 当当前用户名与下一个用户名一致时,说明是一类数据
           为该类数据添加标记 o 数值加一,  并且记录第三次的数值
        3. 当当前用户名与下一个用户名不一致时,说明不是同一类数据
           当该类数据标记小于min_index时则记录最后一次值,否则不记录
           此时将数据标记 o 归零    
    """
    if len(metadata) == num + 1:
        break
    elif metadata[num]['name'] == metadata[num + 1]['name']:
        o += 1
        if o == min_index:
            t_max[g - 1].update({'min_time': metadata[num].get('age')})
    else:
        if o < min_index:
            t_max[g - 1].update({'min_time': metadata[num].get('age')})
        o = 0

    num += 1

print(t_max)
