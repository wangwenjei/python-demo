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


def islogin(func):
    def wrapper(*args, **kwargs):
        print('登录....')
        res = func(*args, **kwargs)
        return res

    return wrapper


@islogin
def login():
    print('登录成功')

login()