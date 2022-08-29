"""
什么是反射:
    指的是程序运行过程中可以动态获取对象的信息


反射内置函数
    hasattr(object,str)  # 判断对象中是否存在该属性
    getattr(object,str,None)  # 获取对象中属性的值
    setattr(object,str,str)  # 修改对象中属性的值
    delattr(object,str)  # 删除对象属性
"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('<%s: %s>' % (self.name, self.age))


obj = People('jason', 18)

# 实现反射机制的步骤
# 1.先通过dir: 查看某一个对象下可以.出那些属性
# print(dir(obj))
# ==> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'say']

# 2.可以通过字符串反射到真正的属性上,得到属性值
# print(obj.__dict__[dir(obj)[-2]])

# 判断是否有该属性值
print(hasattr(obj, 'name'))  # ==> True

# 获取该属性下的值;没有该属性值会报错,此时可以加一个None,没有该属性值返回None
print(getattr(obj, 'name'))  # ==> jason
print(getattr(obj, 'namee', None))  # ==> None

print('=' * 50)
# 修改属性
setattr(obj, 'name', 'www')
print(obj.name)  # ==> www

# 删除属性
delattr(obj, 'name')
print(obj.__dict__)  # ==> {'age': 18}

res1 = getattr(obj, 'say')  # obj.say
res2 = getattr(People, 'say')  # People.say
print(res1)  # ==> <bound method People.say of <__main__.People object at 0x7fe09f6e3fd0>>
print(res2)  # ==> <function People.say at 0x7fe09f612700>


class FTP:
    def put(self):
        print('正在上传')

    def get(self):
        print('正在上传')

    def interface(self):
        method = input('请输入方法:').strip()
        if hasattr(self, method):
            getattr(self, method)()
        else:
            print('无该方法')


obj = FTP()
obj.interface()
#  =>>
# 请输入方法:get   
# 正在上传

print('=== === === === ===')

import abcd
print(getattr('abcd.py', 'Email', None))




