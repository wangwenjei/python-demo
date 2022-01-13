"""
什么是元类:
    用来实例化产生类的类
关系:
    元类 --实例化--> 类(People) --实例化--> 对象(obj)
"""


# 一
class People1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s: %s>' % (self.name, self.age))


obj = People1('jason', 18)

# 查看内置的原类:
# type是内置的元类
# class关键字产生的所有类,都是由内置type实现的
print(type(People1))  # ==> <class 'type'>


# 创建类的过程
# 类的三大特征
# 1.类名
class_name = "People"
# 2.类的基类
class_bases = (object,)
# 3.执行类体代码拿到类的名称空间
class_dic = {}
class_body = """
def __init__(self,name):
    self.name = name
def say(self):
    print(self.name)

"""

exec(class_body, {}, class_dic)
print(class_dic)  # ==> {'__init__': <function __init__ at 0x7fca5cdd4040>, 'say': <function say at 0x7fca5fe1b5e0>}
# 4.调用元类
x = type(class_name, class_bases, class_dic)
print(x)  # ==> <class '__main__.People'>


# 二
# __call__
# 如果想让一个对象加括号就可以被调用,需要在该对象的类中添加一个__call__方法
class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        res = args, kwargs
        return res


obj_c = Foo(1, 2)
res = obj_c('a', 'b', 'c', x=1, y=2, z=3)
print(res)  # ==> (('a', 'b', 'c'), {'x': 1, 'y': 2, 'z': 3})

# 三
#  ========== 自定义元类来控制类的产生 ==========
# 自定义元类来控制类的产生

"""
# People3 = Mymeat(class_name,class_bases,class_dic)
调用Mymeat发生三件事,调用Mymeat就是type.__call__
    1. 先造一个空对象(调用Mymeat类内的__new__方法)  ==> People3 
    2. 调用Mymeat这个类的__init__方法,完成初始化对象的操作
    3. 返回初始化好的对象
    
    
# 对象()  --> 类内的__call__
# 类()  --> 自定义元类内的__call__
# 自定义元类()  -->  内置元类的__call__
"""


class Mymeat(type):  # 只有继承type类的元类才是元类

    def __new__(cls, *args, **kwargs):
        # 造Mymeat对象
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, class_name, class_bases, class_dir):
        """
            print(self)  # ==> <class '__main__.People3'>
            print(class_name)  # ==> People3
            print(class_bases)  # ==> (<class 'object'>,)
            print(class_dir)  # ==>{'__module__': '__main__','__qualname__': 'People3', '__init__': <function People3.__init__ at 0x7fd82361b3a0>, 'say': <function People3.say at 0x7fd82361b310>}
        """
        if not class_name.istitle():  # 做管控类名必须大写,否则抛出异常
            raise NameError('类名首字母必须大写')

        if '__doc__' not in class_dir:  # 做管控类必须写注释,否则抛出异常
            raise TypeError('必须写注释')


# 类的产生
# People3 = Mymeat() ==> type.__call__ ==> 做了三件事:
# 1.type.__call__函数内会先调用Mymeat内的__new__
# 2.type.__call__函数内会先调用Mymeat内的__init__
# 3.type.__call__函数内会返回一个初始化好的对象
class People3(object, metaclass=Mymeat):
    """
        注释
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s: %s>' % (self.name, self.age))


# 类的diaoy
# obj = People3('Jason', 18)  ==> Mymeat.__call__ ==> 做了三件事
# 1.Mymeat.__call__函数内会先调用People3内的__new__
# 2.Mymeat.__call__函数内会先调用People3内的__init__
# 3.Mymeat.__call__函数内会返回一个初始化好的对象


# 四 自定义元类控制类的调用,类的对象的产生
# 模板
class Mymeat(type):
    def __call__(self, *args, **kwargs):
        # 1、Mymeta.__call__函数内会先调用People内的__new__
        classmodule_obj = self.__new__(self)
        # 2、Mymeta.__call__函数内会调用People内的__init__
        self.__init__(classmodule_obj, *args, **kwargs)
        """
        # print('people对象的属性：',classmodule_obj.__dict__)
        此处可以是任意的对类的初始化操作
        """
        classmodule_obj.__dict__['xxx'] = 11111

        # 3、Mymeta.__call__函数内会返回一个初始化好的对象
        return classmodule_obj


class ClassModule(metaclass=Mymeat):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s: %s>' % (self.name, self.age))


obj_module = ClassModule('www', 18)
print(obj_module.__dict__)  # ==> {'name': 'www', 'age': 18, 'xxx': 11111}
