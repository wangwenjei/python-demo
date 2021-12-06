"""
绑定方法( classmethod ): 特殊之处在于将调用者本身当做第一个参数自动传入
    1. 绑定给对象的方法: 调用者是对象,自动传入的是对象
        提供一种新的造对象的方式
    2. 绑定给类的方法: 调用者是类,自动传入的是类

非绑定方法(静态方法):
    没有绑定给任何人: 调用者可以是类,对象,没有自动传参的效果
    按照函数的使用方式

cls: 默认的规范字段
     类下函数通过 classmethod 装饰器将该函数装饰成给类的方法
     cls 用来接收
"""
import settings


class Mysql:
    name = 'jason'

    def __init__(self, ip, port, ):
        print(111)
        self.ip = ip
        self.port = port

    def f1(self):
        print('%s:%s' % (self.ip, self.port))

    @classmethod  # 将下面的函数装饰成绑定给类的方法
    def from_conf(cls, a, b):
        # print(cls)  # ==> <class '__main__.Mysql'>
        print(cls.name)  # ==> jason
        print(a, b)  # ==> 1 2
        return cls(settings.IP, settings.PORT, )

    @staticmethod  # 将下述函数装饰成一个静态方法
    def f2(x, y, z):
        print(x, y, z)


# 传统方式
# obj = Mysql('127.0.0.1', 3306)
# obj.f1()  # ==> 127.0.0.1:3306

# 利用绑定绑定方法 (先执行@classmethod绑定的函数再去执行__init__方法)
obj = Mysql.from_conf(1, 2)
print(obj.__dict__)  # ==> {'ip': '127.0.0.1', 'port': 3306}

# 非绑定方法
# Mysql.f2(1, 2, 3)  # ==> 1 2 3

