"""
什么是继承:
    继承是一种创建新类的方式,新建的类可称之为子类或派生类,父类又可称为基类或超类,子类会继承父类的属性
    Python支持多继承: 新建的类可以继承一个或多个父类
        优点: 子类可以同事继承多个父类的属性,最大限度的重用代码
        缺点: 1.违背人的思维习惯
             2.代码可读性会变差,可能会引发菱形问题
             3.扩展性变差
        不建议使用多继承,如果真的涉及到一个子类不可避免的要重用多个父类的属性,应该使用Mixins机制

为什么要用继承: 用来解决类与类之间代码冗余的问题

Python2 中有经典类与新式类之分
    新式类: 继承了object的子类,以及该子类的子类子子类...
    经典类: 没有继承object的子类,以及该子类的子类子子类...
Python2 中没有继承任何类,那么会默认继承object类,所以Python3中所有的类都是新式类
为了通用性可以再父类中手动添加object
"""


# 单类继承实现
class QHPeople:
    school = "QingHua"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(QHPeople):

    # 在调用父类的基础上并添加新的属性
    def __init__(self, name, age, sex, stu_id):
        QHPeople.__init__(self, name, age, sex)
        self.stu_id = stu_id

    def choose_course(self):
        print("学生 %s 正在选课" % self.name)


# 查看有哪些父类
print(Student.__bases__)  # (<class '__main__.QHPeople'>,)

stu_obj = Student('wwj', 18, 'male', 10001)  # {'name': 'wwj', 'age': 18, 'sex': 'male', 'stu_id': 10001}
print(stu_obj.__dict__)


# 单类继承属性调用
class Foo:
    def f1(self):
        print("Foo.f1")

    def __f2(self):
        print("Foo.f2")

    def f3(self):
        print("Foo.f3")
        # 直接调用时,调用的是对象中的函数
        # self.f1()  # obj.f1()  ==>  Bar.f1
        # self.f2() # obj.f2()  ==>  Bar.f2

        # 想要调用当前类中的方法
        Foo.f1(self)  # 方法一: ==> Foo.f1   但是使用该方法的话,调用类需要接收什么参数都必须一一传入
        self.__f2()  # 方法二:  ==> Foo.f5   使用该方法则不要传入参数,原理是,该函数名发生形变 _Foo__f5


class Bar(Foo):
    def f1(self):
        print("Bar.f1")

    def f2(self):
        print("Bar.f2")


obj = Bar()
obj.f3()

"""
在子类派生的新方法中重用父类的功能
    方式一: 指名道姓调用某一个类下的函数,不依赖于继承关系
    方式二: 利用 super()函数 调用父类提供给自己的方法,严格依赖继承关系
           调用super()会得到一个特殊的对象,该对象会参照发起属性查找的那个类的mro,去当前类的父类中找属性
"""


# 方式一:
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('hello %s' % self.name)


class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        People.__init__(self, name, age, sex)
        self.level = level
        self.salary = salary


ted_obj = Teacher('www', 18, 'male', 10, 3000)
print(ted_obj.__dict__)  # ==> {'name': 'www', 'age': 18, 'sex': 'male', 'level': 10, 'salary': 3000}

# 方式二:
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('hello %s' % self.name)


class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex)
        self.level = level
        self.salary = salary

print(Teacher.mro())
ted_obj = Teacher('www', 18, 'male', 10, 3000)
print(ted_obj.__dict__)  # ==> {'name': 'www', 'age': 18, 'sex': 'male', 'level': 10, 'salary': 3000}

