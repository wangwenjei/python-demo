"""
数字类型
    1. 整型 int
        用来记录类似年龄,人数,班级数等个数时
    2. 浮点型 float
        用来记录类似成绩,身高,薪资等带小数的数时

int(x,[base])	将x转换为一个整数,默认10十进制
long(x,[base]) 	将x转换为一个长整数
float(x)	将x转换到一个浮点数
"""

# 1.int 整型
age = 18

# 2. float 浮点型
height = 1.87

# 转换类型
height1 = int(height)
print(type(height1))  # ==> <class 'int'>

# 运算
print(10 + 2.5)  # ==> 12.5
print(10 < 2.5)  # ==> False
