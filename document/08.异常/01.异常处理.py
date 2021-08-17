"""
什么是异常:
    异常是程序发生错的信号,程序一旦出错就会抛出异常,程序的运行随即终止
异常处理:
    为了增强程序的健壮性,即便是程序运行过程中出错了,也不要终止程序,而是去捕捉异常并处理(将出错信息记录到日志内)

语法:
    try:
        子代码块 #有可能会抛出异常的代码
    except 异常类型1 as e:
        pass
    except 异常类型2 as e:
        pass
    else:
        如果被检测的子代码块没有异常,则会执行else的子代码
    finally:
        无论被检测的子代码块有无异常,都会执行finally的子代码

else 不能单独与try配合使用,必须搭配except
finally: 可以单独与try配合使用
         不处理异常,无论是否发生异常都会执行finallyd的子代码
         被检测代码中回收系统资源的代码可以放到finally中,确保资源可以被回收
"""

try:
    print('111111')
    l = ['aaa', 'bbb']
    # l[3]  # 抛出 IndexError 异常, 该代码同级别的后续代码不会运行
    print('222222')
    xxx
    print('333333')
    dic = {'a': 1}
    dic['aa']

except (IndexError, NameError) as e:
    print('异常信息:', e)
# except KeyError as e:
#     print('字典的Key不存在:', e)
except Exception as e:  # Exception 万能异常,所有的异常都可以匹配上
    print('所有的异常都可以匹配到', e)

