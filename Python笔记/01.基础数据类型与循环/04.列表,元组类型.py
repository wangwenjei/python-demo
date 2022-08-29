"""
列表类型: list  有序类型
    索引对应值，索引从0开始，0代表第一个
    作用：按位置记录多个值（同一个人的多个爱好、同一个班级的所有学校姓名、同一个人12个月的薪资），并且可以按照索引取指定位置的值
    定义：在[]内用逗号分隔开多个任意类型的值,一个值称之为一个元素
                  0     1     2     3
            l = [100, 19.25, 'a', [1, 2]]
    索引反映的是顺序、位置，对值没有描述性的功能

常用内置方法:
    list.append(obj)   在列表末尾添加值
    list.insert(index,obj)   执行索引位置添加值

    list.extend(seq)    将一个可循环对象,取出值添加到列表中
                        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）


    del list[index]    根据索引通用删除,且不支持赋值
    list.pop(index)    根据索引删除,不指定索引默认选择最后一个,返回值为删除的值
    list.remove(obj)   根据元素删除,返回值为None

    list.count(obj)    统计列表中某一元素出现的累计次数
    list.index(obj)    统计列表中某一元素第一次出现的索引值,找不到则报错

    list.reverse()     将列表倒过来

    list.clear     清空列表

    l.sort()	将列表排序,默认升序(reverse=True 为降序)



 队列(FIFO):先进先出
 堆栈(LIFO):后进先出
"""

a = [1, 2, 3, 4, 5]

a.append('wwj')
print(a)  # ==> [1, 2, 3, 4, 5, 'wwj']

a.insert(3, 'www')
print(a)  # ==> [1, 2, 3, 'www', 4, 5, 'wwj']

b = ['a', 'b', 'c']
a.extend(b)
print(a)  # ==> [1, 2, 3, 'www', 4, 5, 'wwj', 'a', 'b', 'c']

del a[3]
print(a)  # ==> [1, 2, 3, 4, 5, 'wwj', 'a', 'b', 'c']

a.pop(3)
print(a)  # ==> [1, 2, 3, 5, 'wwj', 'a', 'b', 'c']

a.remove('c')
print(a)  # ==> [1, 2, 3, 5, 'wwj', 'a', 'b']

print(a.count(1))  # ==> 1
print(a.index('wwj'))  # ==> 4

a.reverse()
print(a)  # ==> ['b', 'a', 'wwj', 5, 3, 2, 1]

a.clear()
print(a)  # ==> []

l = [4, 2, 6, 1, 3, 5]
l.sort()
print(l)  # ==> [1, 2, 3, 4, 5, 6]

# 循环打印
# for i in [1, 2, 3]:
#     print(i)  # ==> 1 2 3


"""
元组类型: tuple
    元组: 一个不可变的列表
    作用: 按照索引/位置存放多个值,只用于读不用于改
    注意: 如果元组中只有一个元素,必须加逗号分隔 t=(9, )  否则将不是元组类型
    

"""

t = (1, 2, 3)
print(type(t))  # ==> <class 'tuple'>
