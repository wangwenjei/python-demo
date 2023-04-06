"""
可变长度的参数(*与**)
    可变长度指的是在函数调用时,传入的值个数不固定,
    而实参是用来为形参赋值的,需要一一对应,针对溢出的实参必须要有对应的形参来接收


可变长度的位置参数(*): 用来接收溢出的位置实参

    *形参名:  用来接收溢出的位置实参,溢出的位置实参会被*保存成元组的格式,然后复制给紧跟其后的形参名,
             *后跟的形参名可以是任意名称,但约定俗成的是args
    * 可在实参中: 实参中带*,先将 * 后的值打散成位置实参
    形参与实参都带* :  先打散再将溢出的值保存为元组

可变长度的关键字参数(**): 用来接收溢出的关键字实参
    **形参名: 用来接收溢出的关键字实参,**会将溢出的关键字实参保存成字典格式,然后赋值给紧跟其后的形参名,
             **后跟的形参名可以是任意名称,但约定俗成的是kwargs

    ** 可用在实参中:  实参中带**,先将**后的值打散成关键字实参,
                    **在是实参中其后只能跟字典类型

    形参与实参都带**:  先打散再将溢出的值保存为字典


* 与 ** 混用:
    *args 必须在 **kwargs 前
"""


# *args 用法
def func(*args):
    print(args)


func(1, 2, 3)  # ==> (1, 2, 3)


def sum(*args):
    num = 0
    for i in args:
        num += i
    print(num)


sum(1, 2, 3)  # ==> 6


# *在实参中用法
def func(x, y, z):
    print(x, y, z)


func(*[11, 22, 33])  # ==> 11 22 33


# *args 与 *在实参中混用
def func(x, y, *args):
    print(x, y, args)


func(1, 2, *[3, 4, 5])  # ==> 1 2 (3, 4, 5)


# **kwargs 用法
def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3)  # ==> {'a': 1, 'b': 2, 'c': 3}


# **在实参中用法
def func(x, y, z):
    print(x, y, z)


func(**{'x': 1, 'z': 2, 'y': 3})  # ==> 1 3 2


# **kwargs与**在实参中混用
def func(x, y, **kwargs):
    print(x, y, kwargs)


func(**{'x': 1, 'y': 2, 'a': 3, 'b': 4, 'c': 5})  # ==>  1 2 {'a': 3, 'b': 4, 'c': 5}


# * 与 **

def func(*args, **kwargs):
    print(args, kwargs)


func(1, 2, 3, x='a', y='b', z='c')  # ==> (1, 2, 3) {'x': 'a', 'y': 'b', 'z': 'c'}

print('=' * 50)


# *args,**kwargs 与 *在实参中 以及 **在实参中混用
def index(x, y, z):
    print('index=>>> ', x, y, z)


def wrapper(*args, **kwargs):  # => (1,) {'z': 3, 'y': 2}
    index(*args, **kwargs)  # ==> index(1, z=3, y=2)


wrapper(1, z=3, y=2)  # ==> index=>>>  1 2 3
