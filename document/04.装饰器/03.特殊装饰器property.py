"""
# property 是一个装饰器,是用来将绑定给对象的方法伪造成一个数据属性
我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改
day29
"""


class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


# obj = People('wwj', 70, 1.83)  # 20.902385858042937
#
#
# print(obj.bmi)

####################################################################

class People2:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, val):
        if val is not str:
            print('只接收str类型')
        self.__name = val

    def del_name(self):
        print('不许删')

    name = property(get_name, set_name, del_name)


# obj2 = People2('wwj')
#
# print(obj2.name)  # wwj
# obj2.name = 18  # 只接收str类型
# del obj2.name  # 不许删


####################################################################

class People3:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if val is not str:
            print('只接收str类型')
        self.__name = val

    @name.deleter
    def name(self):
        print('不许删')


obj3 = People3('wwj')

print(obj3.name)  # wwj
obj3.name = 18  # 只接收str类型
del obj3.name  # 不许删
