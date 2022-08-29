"""
菱形继承出现: 一个子类继承的多个父类最终汇聚到一个非object类
            D 类继承 B类和C类  B类与C类又分别继承于A类
class A():
class B(A):
class C(A):
clas D(B,C):
            A
          B   C
            D

mro() 方法: 可用来查看继承的检索优先顺序
    新式类内置了mro方法可以查看线性列表的内容，类的继承查找顺序按照mro查询的列表,经典类没有该内置该方法
    特点:
        1.类相关的属性查找(类名.属性,该类的对象.属性),参照的都是该类的mro
        2.子类会优先于父类被检查
        3.多个父类会根据它们在列表中的顺序被检查
        4.如果对下一个类存在两个合法的选择,选择第一个父类

如果多继承是非菱形继承,经典类 与 新式类  的属性查找顺序是一样:
    都是一个分支一个分支的找下去,然后最后找object

如果多继承是菱形继承,经典类 与 新式类 的属性查找顺序不一样:
    经典类: 深度优先(在检索第一条分支的时候就直接一条道走到黑,即会检索最终的那个共同的公共父类)
    新式类: 广度优先(在检索最后一条分支的时候才会检索那个共同的公共父类)
    class G():
    class E(G):
    class F(G):
    class B(E):
    class C(F):
    class D(G):
    class A(B,C,D):
    经典类: A -> B -> E -> G -> C -> F -> D -> object
    新式类: A -> B -> E -> C -> F -> D -> G -> object
"""


# 菱形问题
class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B, C):
    pass


obj = D()
obj.test()  # ==> from B

print(D.mro())  # 类D以及类D的对象访问属性都是参照该类的mro列表
# D -> B -> C -> A -> object
# ==> [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


"""
多继承
使用多继承应当遵循 Mixins机制
Mixins机制核心: 就是在多继承背景下尽可能的提升多继承的可读性

的命名方式一般以 Mixin, able, ible 为后缀
"""


class Vehicle:  # 交通工具
    pass


class FlyableMixin:
    def fly(self):
        """
            飞行功能相应的代码
        """
        print("I am flying")


class CivilAircraft(FlyableMixin, Vehicle):  # 民航飞机
    pass


class Helicopter(FlyableMixin, Vehicle):  # 直升飞机
    pass


class Car(Vehicle):  # 汽车
    pass

# ps: 采用某种规范（如命名规范）来解决具体的问题是python惯用的套路
