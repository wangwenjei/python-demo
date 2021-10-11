"""
字典类型: dict
    定义: d = {key:value}
    赋值: key存在则修改,不存在则添加
    取值: d[key]

成员运算根据key进行

常用内置方法:
    dict.pop(key)     根据key删除元素,返回删除key对应的那个value值
    dict.popitem()    随机删除,返回元组(删除的 key 与 value)

    dict.update(dict2)  将dict2中的key:value更新到dict中, dic中不存在的key添加, dict存在的key以 dict2 中的值准

    dict[key]   普通字典取值,key没有会报错
    dict.get(key)  get取值,key没有会返回None

    dict.setdefault(key,default=None)  如果key有值则不添加, 没有值则添加键 并将值设为default的值,默认为None

    dict.keys()    以列表返回一个字典所有的键
    dict.values()  以列表返回字典中的所有值

    dict.clear()  清理字典

    items() 函数以列表返回字典所有键值对

"""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# d.pop('b')
# print(d)  # ==> {'a': 1, 'c': 3, 'd': 4}

# print(d)
d1 = {'x': 1, 'y': 2, 'a': 999}

d.update(d1)
print(d)  # ==> {'a': 999, 'b': 2, 'c': 3, 'd': 4, 'x': 1, 'y': 2}

print(d['a'])  # ==> 999
print(d.get('a'))  # ==> 999

d.setdefault('name','wwj')
d.setdefault('aaa')
print(d)  # ==> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'name': 'wwj', 'aaa': None}

d.clear()
print(d)  # ==> {}

course_list_msg = {'QH': ['Python', 'Java', 'GO'], 'BD': ['LINUX', 'Python']}
a = list(course_list_msg.keys())
print(list(a))   # ==> ['QH', 'BD']

a1 = {1: 'a', 2: 'b', 3: 'c'}
print(a1.items())  # ==> dict_items([(1, 'a'), (2, 'b'), (3, 'c')])

for key, value in a1.items():  # 当只有一个变量接收参数时,打印元组 (1, 'a') ...
    print(key, value)
# ==>
# 1 a
# 2 b
# 3 c

"""
集合类型: set
    集合内元素必须为不可变类型,
    集合内元素无序,
    集合内元素没有重复值,
    比较大小是比较是否是包含关系
        
利用集合去重: 只能针对不可变类型去重,无法保证原来的顺序

关系运算:
    取交集:
        set = set1 & set2 
        set = set1.intersection(set2)    
    
    取并集:
        set = set1 | set2
        set = set1.union(set2)
    
    取差集: 取差集有左右之分
        set = set1 - set2
        set = set1.difference(set2)
    
    对称差集:
        set = set1 ^ set2
        set = set1.symmetric_difference(set2)
    
    父子集:
        set1 > set2
        set1.issuperset(set2)
        
        
        
常用内置方法:
    set.discard()   将一个元素从集合中删除,不存在不会报错
    set.remove()    将一个元素从集合中删除,删除元素不存在会报错
    set1.update(set2)   将set2加入到set1中,并去重
"""

f1 = {'a', 'b', 'c'}
f2 = {'e', 'f', 'c'}

# 交集
c = f1 & f2
c1 = f1.intersection(f2)
print(c, c1)  # ==> {'c'} {'c'}

# 并集
c = f1 | f2
c1 = f1.union(f2)
print(c, c1)  # ==> {'f', 'a', 'c', 'b', 'e'} {'f', 'a', 'c', 'b', 'e'}

# 差集
c = f1 - f2
c1 = f1.difference(f2)
print(c, c1)  # {'b', 'a'} {'b', 'a'}

c = f2 - f1
print(c)  # ==> {'e', 'f'}

# 对称差集
c = f1 ^ f2
c1 = f1.symmetric_difference(f2)
print(c, c1)  # ==> {'e', 'f', 'b', 'a'} {'e', 'f', 'b', 'a'}

# 父子集
s1 = {1, 2, 3}
s2 = {1, 2}

print(s1 > s2)  # ==> True
print(s1.issuperset(s2))  # ==> True
print(s1.issubset(s2))  # ==> False

f1.discard('a')
print(f1)  # ==> {'b', 'c'}

f1.remove('c')
print(f1)  # ==> {'b'}

f1.update(f2)
print(f1)  # ==> {'b', 'e', 'c', 'f'}
