"""
类是对象相似数据与功能的集合体,
所以类中最常见的是变量与函数的定义,但是类体其实可以包含任意其他
类体代码是在类定义阶段就会立即执行,会产生类的名称空间

为什么要用类: 用来解决对象间代码冗余的问题

self: 默认的规范字段,用来接收调用对象,什么对象调用就传入该实例化对象的名称
"""


class Student1:
    stu_school = 'QingHua'

    def func(self):
        pass


# 属性访问语法
#  访问数据数据属性
print(Student1.stu_school)  # 等同于 print(Student.__dict__['stu_school'])

#  访问函数属性
print(Student1.func)  # ==> <function Student1.func at 0x7f90d061b700>

# 为类添加参数
Student1.xxx = 'www'
print(Student1.__dict__)
#  ==>
"""
{'__module__': '__main__', 
 'stu_school': 'QingHua', 
 'func': <function Student1.func at 0x7ff22dad91f0>,
 '__dict__': <attribute '__dict__' of 'Student1' objects>, 
 '__weakref__': <attribute '__weakref__' of 'Student1' objects>,
 '__doc__': None, 
 'xxx': 'www'}
"""

'''
    调用类产生对象
'''


class Student2:
    stu_school = 'QingHua'

    def __init__(self, name, age, gender):  # 接收变量的参数与调用类时传入的参数一一对应
        self.stu_name = name
        self.stu_age = age
        self.stu_gender = gender

    def tell_stu_info(self):
        print('学生信息:名字: %s,年龄: %s,性别: %s' % (
            self.stu_name,
            self.stu_age,
            self.stu_gender
        ))


"""
调用类产生对象,为不同的对象赋值不同的参数
调用类的过程又称之为实例化,会发生三件事
    1.先产生一个空对象
    2.Python会自动调用类中的__init__方法,
      然后将空对象调用类时括号内传入的参数一同传给__init__方法
    3.返回初始化完的对象

__init__方法
    1.会在调用类时自动触发执行,用来为对象初始化自己独有的数据
    2.__init__内应该存放对象初始化属性的功能,但也可以存放其他任意代码
      想要在类调用时立即执行的代码都可存放在__init__方法内
    3.__init__方法必须返回None

关于类的调用
   1. 类的数据属性是共享给所有对象使用,访问地址都一样
   2. 类中定义的函数主要是给函数使用的,而且是绑定给对象的,虽然说有对象指定的都是相同的功能,当绑定到不同的对象就是不同的绑定方法,内存地址各不相同
   3. 类调用自己的函数属性必须严格按照函数的用法来使用
    类的函数属性是绑定给对象用的

绑定方法的特殊之处在于: 谁来调用绑定方法就会将谁当做第一个参数自动传入
"""
# 实例化一个 stu1_obj 对象
stu1_obj = Student2('wwj', 18, 'male')

# print(stu1_obj.__dict__)  # {'stu_name': 'wwj', 'stu_age': 18, 'stu_gender': 'male'}
# print(stu1_obj.stu_school)  # QingHua 先从对象中找,没有再从类中找

# 通过类调用 (推荐使用 绑定方法 来调用)
Student2.tell_stu_info(stu1_obj)  # 学生信息:名字: wwj,年龄: 18,性别: male

# 通过绑定方法调用
stu1_obj.tell_stu_info()  # 学生信息:名字: wwj,年龄: 18,性别: male

# 打印类的名字
print(stu1_obj.__class__.__name__)  # ==> Student2
