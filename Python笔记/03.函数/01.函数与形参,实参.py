"""
函数:

为什么要用函数: 用来解决代码冗余的问题

函数分为:
    1.无参函数
    2.有参函数
    3.空函数: 函数体代码为pass

函数使用:
    可以把函数当成变量使用
    可以赋值
    可以当做函数的参数传入给另外一个函数
    可以当做函数另外一个函数的返回值
    可以当做容器类型的一个元素
"""


def func():
    print("无参函数")


func()  # ==> 无参函数


def func(x, y):
    print("有参函数: x=%s y=%s" % (x, y))


func(1, 2)  # ==> 有参函数: x=1 y=2


def func():  # 空函数
    pass


"""
形参与实参:
    形参: 在定义函数阶段定义的参数称之为形势参数,简称形参,相当于变量名
    实参: 在调用函数阶段传入的值称之为实际参数,简称实参,相当于变量值
    
形参与实参的关系:
    在调用阶段,实参的值会绑定给形参;
    这种绑定关系只能在函数体内使用;
    实参与形参的绑定关系在函数调用时生效,函数调用结束后解除绑定关系
    
形参与实参的使用:
    1.位置参数: 按照从左到右的顺序依次定义的参数称之为位置参数
        1.1: 位置形参: 必须被传值,且多一个不行,少一个也不行
        1.2: 位置实参: 按照顺序与位置形参成一一对应关系
    2.关键字参数: 在函数调用阶段,按照 key=value 的形式传入值,指名道姓的给某个形参传值,可以与形参顺序不一致
    3.默认参数: 在函数定义阶段,为形参赋值,称之为默认参数,在调用阶段可不为形参赋值
    
位置实参与关键字参数混用:
    关键字实参必须在位置实参的右侧
   
位置形参与默认参数混用:
    位置形参必须在默认形参左侧
    默认参数的值是在函数定义阶段被复制的,准确的说被赋予的是值的内存地址 
    虽然默认参数的值可以被指定为任意数据类型,但是不推荐使用可变类型

函数最理想的状态: 函数的调用只跟函数体本身有关系,不受外界代码影响

"""


def func(x, y, v, k, j=9):
    print(f"位置参数 x=%s,y=%s 关键字参数:v=%s k=%s 默认参数:{j}" % (x, y, v, k))


func(1, 2, k="a", v="b")  # ==> 位置参数 x=1,y=2 关键字参数:v=b k=a 默认参数:9


def func(x, y, z, l=None):
    if l is None:
        l = []
    l.append(x)
    l.append(y)
    l.append(z)
    print(l)


func(1, 2, l=['a'], z=3)  # ==> ['a', 1, 2, 3]

"""
函数类型提示:
"""


# 提示 name 应该接收str 类型, 冒号后是提示信息,提示信息可以是任意字符或表达式
# -> int 提示返回值应该是int 类型, -> 后接的是提示函数返回值信息,提示信息可以是任意字符或表达式
def func(name: str, age: int, hobbies: tuple) -> int:
    print('我叫 %s 今年 %s 岁 爱好是 %s' % (name, age, hobbies))
    return 111


func(name='wwj', age=18, hobbies=('basketball', 'football'))  # ==> 我叫 wwj 今年 18 岁 爱好是 ('basketball', 'football')


# 为函数添加默认参数
def func(name: str = 'wwj', age: int = 18, hobbies: tuple = ('basketball',)) -> int:
    print('我叫 %s 今年 %s 岁 爱好是 %s' % (name, age, hobbies))
    return 111


func()  # ==> 我叫 wwj 今年 18 岁 爱好是 ('basketball',)

# 查看函数提示信息
print(func.__annotations__)
# ==> {'name': <class 'str'>, 'age': <class 'int'>, 'hobbies': <class 'tuple'>, 'return': <class 'int'>}
