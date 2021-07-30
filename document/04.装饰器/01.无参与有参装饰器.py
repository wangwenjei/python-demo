"""
装饰器:
    定义一个函数,该函数是用来为其他函数添加额外的功能
    装饰器就是在不修改被装饰器对象源码以及调用方式的前提下为被装饰对象添加新功能

为什么要用装饰器:
    开放封闭原则:
        开放: 指的是对拓展功能是开发的
        封闭: 指的是对修改源代码是封闭的

"""

# 无参装饰器
"""
无参装饰器模板:
def outter(func):  # 装饰器
    def wrapper(*args,**kwargs):
        1. 调用原函数
        2. 为其增加新功能
        res = func(*args,**kwargs)   # 调用原函数
        return res
    return wrapper
    
@outter   # 调用装饰器
def index():   # 被装饰对象
    函数体代码
    
index()
"""
import time


def outter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print("timeout:", stop - start)
        return res

    return wrapper


@outter  # 在被装饰器对象正上方的单独一行写 @装饰器名字 等同于 index = outtter(index)
def index():
    time.sleep(1)
    return '被装饰对象'


print(index())

# 有参装饰器
"""
有参装饰器模板:
def auth(x,y,z):
    def outter(func):
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            return res
        return wrapper
    return outter
    
@auth(x=1,y=2,z=3)
def index():
    函数体代码

index()
"""


def auth(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            name = input("you name>>>:").strip()
            passwd = input("you passwd>>>:").strip()

            if db_type == 'file':
                print('基于文件验证')
                if name == "wwj" and passwd == "123":
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("user or password error")

            if db_type == 'mysql':
                return '基于MySQL验证'

            return '不支持该验证方法'

        return wrapper

    return deco


@auth(db_type='file')
def index(x, y):
    return "index===>%s,%s" % (x, y)


print(index(x=1, y=2))
