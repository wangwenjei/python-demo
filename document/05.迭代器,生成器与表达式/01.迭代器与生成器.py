"""
迭代器: iter()
    迭代器指的是迭代取值的工具,迭代是一个重复的过程,
    每次重复都是基于上一次的结果而继续,单纯的重复并不是迭代,
    迭代器是用来迭代取值的工具,涉及到把多个值循环取出的类型有: 列表,字符串,元组,字典,集合,打开的文件

为了解决基于索引迭代器取值的局限性

可迭代对象: 但凡内置有  __iter__  方法的都可称之为可迭代对象
"""

d = {'a': 1, 'b': 2, 'c': 3}
d_iter = d.__iter__()  # 转换为可迭代

# print(d_iter.__next__())  # ==> a
# print(d_iter.__next__())  # ==> b
# print(d_iter.__next__())  # ==> c
# print(d_iter.__next__())  # ==> 抛出异常StopIteration


"""
生成器:  自定义的迭代器

生成器的关键点在与 yield 的使用

函数体代码在运行时遇到 yield 会停下来,并将本次 yield 后产生的值 当做本次调用的返回值返回
"""


def ma_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


# g = ma_range(1, 5, 2)
# g = g.__iter__()
# print(g.__iter__().__next__())  # ==> 1
# print(g.__iter__().__next__())  # ==> 3
# print(g.__iter__().__next__())  # ==> 抛出异常StopIteration

for i in ma_range(1, 5, 2):
    print(i)  # ==> 1  3


# 表达式形式
def dog(name):
    print('道哥 %s 准备吃东西了....' % name)

    while True:
        x = yield  # 相当于 x = 热包子
        print('道哥 %s 吃了 %s' % (name, x))


g = dog('alex')
g.send(None)  # 道哥 alex 准备吃东西了....  =====> 将生成器挂起
g.send('热包子')  # 道哥 alex 吃了 热包子    =====> 将热包子传给 yield
g.send('烧麦')  # 道哥 alex 吃了 烧麦       =====> 将烧麦传给 yield
g.close()  # ====> 关闭后就无法再传值
# g.send('大棒骨')  # =====> 抛出异常 StopIteration
