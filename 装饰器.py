def deco1(func1):  # func1 = wrapper2内存地址
    def wrapper1(*args, **kwargs):
        print('开始运行====>deco1.wrapper1')
        res = func1(*args, **kwargs)
        print('结束运行====>deco1.wrapper1')
        return res

    return wrapper1


def deco2(func2):  # func2 = wrapper3内存地址
    def wrapper2(*args, **kwargs):
        print('开始运行====>deco2.wrapper2')
        res = func2(*args, **kwargs)
        print('结束运行====>deco2.wrapper2')
        return res

    return wrapper2


def deco3(x):
    def outter3(func3):  # func3 = 被装饰对象index函数的内存地址
        def wrapper3(*args, **kwargs):
            print('开始运行====>deco3.outter3.wrapper2')
            res = func3(*args, **kwargs)
            print('结束运行====>deco3.outter3.wrapper2')
            return res

        return wrapper3

    return outter3


@deco1  # idnex = outter(wrapper2内存地址)    ==> index = wrapper1内存地址
@deco2  # index = outter2(wrapper3内存地址)   ==> index = wrapper2内存地址
@deco3(111)  # =>> @outter3 =>> index=outter3(index) ==> index=wrapper3内存地址
def index(x, y):
    print('from index %s %s' % (x, y))


index(1, 2)
# 结论:
# 叠加多个装饰器的加载顺序与运行顺序
# 	加载顺序是自下而上(了解)
# 	执行顺序是
# 		自上而下 即 wrapper1 >>> wrapper2 >>> wrapper3

#### ++++ ####
# 开始运行====>deco1.wrapper1
# 开始运行====>deco2.wrapper2
# 开始运行====>deco3.outter3.wrapper2
# from index 1 2
# 结束运行====>deco3.outter3.wrapper2
# 结束运行====>deco2.wrapper2
# 结束运行====>deco1.wrapper1
