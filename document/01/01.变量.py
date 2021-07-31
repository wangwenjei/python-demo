"""
什么是变量: 可以变化的量,比如年龄,收入,等级等
变量的使用: 先定义,后使用
变量的组成部分:
    1. 变量名: 是指向等号右侧值的内存地址,用来访问等号右侧的值
            命名规则:
                1. 只能是字母,数字,下划线的任意组合
                2. 变量名的第一个字符不能是数字
                3. Python中的关键字不能被声明为变量名

            命名风格:
                变量:
                    1. 纯小写加下划线的方式(在python中，关于变量名的命名推荐使用这种方式)
                    2. 驼峰题
                常量(不变的量): python语法中没有常量的概念，但是在程序的开发过程中会涉及到常量的概念
                    1. 通常将 小写字母全为大写代表常量

    2. 赋值符号(=): 将变量值的内存地址绑定给变量名

    3. 变量值: 任意数据类型,函数,类等,用来记录事务的状态

   name = 'wwj'  等号左边为定义的变量名,右边是为变量名定义赋的值

内存管理(垃圾回收机制):
    垃圾: 当一个变量被绑定的变量名的个数(引用计数)为0时,该变量值无法被访问到,称之为垃圾

引用计数: 当引用计数变为0时,就会被定义为垃圾

is 与 ==:
    is: 比较is左右两边两个值的 id 是否相等
    ==: 比较is左右两边两个值的 值 是否相等

    id不同的情况下,值有可能相同,即两块不同的内存空间里可以存相同的值
    id相同的情况下,值一定相同, x is y 成立 则 x == y 必然成立


"""

# 引用计数
# 引用计数增加
x = 10  # 10的引用计数为1    x = 10的内存地址
y = x  # 10的引用计数为2     y = 10的内存地址
z = x  # 10的引用计数为3     z = 10的内存地址

# 引用计数减少
del x  # 解除变量名x与值10的绑定关系，10的引用计数变为2
del y  # 10的引用计数变为1
z = 12345  # # 10的引用计数变为0
print(z)  # ==> 12345

# 变量的特性
name = "wwj"
# id(): 反映的是变量的内存地址,内存地址不用则id不同
print(id(name))  # ==> 140457342711472
# type(): 展示变量的类型,不同类型的值用来表示记录不同的状态
print(type(name))  # ==> <class 'str'>
# 打印出变量值本身
print(name)  # ==> wwj
