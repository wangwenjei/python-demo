"""
多态:
    什么是多态:  同一种事务有多种形态
    多态性指的是可以在不考虑对象具体类型的情况下而直接使用对象

Python推荐使用鸭子类型实现多态
"""


# 利用继承实现多态
class Animal:  # 同一类事物:动物
    def talk(self):
        print('动物基本的发声频率...', end='')


class Cat(Animal):  # 动物的形态之一:猫
    def talk(self):
        super().talk()
        print('喵喵喵')


class Dog(Animal):  # 动物的形态之二:狗
    def talk(self):
        # super().talk()
        super(Dog, self).talk()
        print('汪汪汪')


class Pig(Animal):  # 动物的形态之三:猪
    def talk(self):
        super(Pig, self).talk()
        print

    pass


# 实例化得到三个对象
cat = Cat()
dog = Dog()
pig = Pig()


# 定义一个统一接口来使用
def Talk(animal):
    animal.talk()


Talk(cat)

'''
# 鸭子类型实现多态  Python推崇的这种方法
'''


class Cpu:
    def read(self):
        print('cpu read')

    def write(self):
        print('cpu write')


class Mem:
    def read(self):
        print('mem read')

    def write(self):
        print('mem write')


class Txt:
    def read(self):
        print('txt read')

    def write(self):
        print('txt write')


obj_cpu = Cpu()
obj_men = Mem()
obj_txt = Txt()

# obj_cpu.read()  # ==> cpu read
# obj_cpu.write()  # ==> cpu write
# obj_men.read()  # ==> mem read
# obj_men.write()  # ==> mem write
# obj_txt.read()  # ==> txt read
# obj_txt.write()  # ==> txt write

'''
# 了解
# 利用抽象基类强制子类必须遵从父类中的方法
'''
import abc


class Animal1(metaclass=abc.ABCMeta):  # 统一所有子类的方法
    @abc.abstractmethod  # 增加该装饰器后就硬性规定了所以子类必须要有 say() 方法否则将报错
    def say(self):
        print('say')

    def talk(self):
        print('talk')


class Dog(Animal1):
    def say(self):
        pass


obj1 = Dog()
obj1.say()
obj1.talk()
