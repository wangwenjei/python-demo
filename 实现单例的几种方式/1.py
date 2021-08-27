
#
# https://www.cnblogs.com/huchong/p/8244279.html
#

# 方式一: 使用模块的方式
# from mysingleton import singleton
#
# print(singleton is singleton)  # ===> True

#
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)