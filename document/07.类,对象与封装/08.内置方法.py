"""
什么是内置方法:
    定义在类内部,以__开头,__结尾的方法
    特点: 会在某种情况下自动触发执行

为什么要用内置方法:
    为了定制化类或对象

__str__: 在打印对象时会自动触发,然后将返回值(必须是字符串类型)当做本次打印的结果输出
__del__: 在清理对象时触发,会先执行该方法

"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # 占用的是操作系统的资源
        self.x = open(r'./settings.py', mode='rb')

    def __str__(self):
        # return '<%s: %s>' % (self.name, self.age)
        return str(self.__dict__)

    def __del__(self):  # 不主动调用会在程序结束时自动调用
        # print('xxx')
        self.x.close()  # 是否内存


obj = People('jason', 18)
print(obj)  # ==> {'name': 'jason', 'age': 18}

print('=====>')
