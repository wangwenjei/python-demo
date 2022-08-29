"""
将封装的属性进行隐藏操作
    如何隐藏: 在属性名前加__前缀,就会实现一个对外隐藏属性效果

    该隐藏方式需要注意:
        1.在类外部无法直接访问__开头的属性,但在知道类名与属性名后可以拼出名字: _类名__属性名 继而使其能够访问
          所以严格意义上来说该种隐藏只是语法上的一种变形,并没有严格的限制外部访问
        2.这种隐藏对外不对内,因为__开头的属性会在 检查类体内代码语法时 统一发生变形
        3.这种变形操作只会在检查类体语法的时候发生一次,之后定义的__开头的属性都不会发生变形

    为什么要隐藏属性:
        1.隐藏数据属性
            将数据隐藏起来就限制了类外部对数据的直接操作,
            通过类内部提供相应接口来允许类外部对数据进行间接操作,
            接口之上可以通过额外附加逻辑对数据进行控制

        2.隐藏函数属性
            当某些函数只需要对类内部提供功能时,此时可隐藏该类函数,目的是为了隔离复杂度,减轻调用者使用者难度
"""


class Foo:
    __x = 1  # 属性名发生变形 _Foo__x = 1
    y = 2

    def __func(self):  # 属性名发生变形 _Foo__func
        print('func')

    def check_x(self):
        print(self.__x)  # print(self._Foo__x)

    def check_y(self):
        print(self.y)


# print(Foo._Foo__x)  # 1
obj1 = Foo()
obj1.check_x()  # 1
obj1._Foo__func()  # ==> func  由此可见Python中并没有强制的隐藏

# 直接对数据做了修改
Foo.y = 3
Foo().check_y()  # 3


# 隐藏数据类型
class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print(self.__name)

    def set_name(self, val):
        if type(val) is not str:
            print('只接收str类型')
            return
        self.__name = val


obj2 = People('wwj')
obj2.get_name()  # wwj
obj2.set_name(111)  # 只接收str类型

print(property)
