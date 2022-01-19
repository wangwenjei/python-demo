from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app03 import models

    "增"
    # res = models.User.objects.create(name='jason', age=18, register_time='2021-01-01')
    # print(res)  # ===> User object (2)  返回值就是被创建的对象本身

    # import datetime
    # ctime = datetime.datetime.now()
    # user_obj = models.User(name='jason2', age=18, register_time=ctime)
    # user_obj.save()

    "删"
    # res = models.User.objects.filter(pk=6).delete()
    # print(res)  # ==> (1, {'app03.User': 1})  1 是影响的行数
    """
        pk 会自动查找当前表的主键字段, 指代的就是当前表的主键字段
        用来pk后 就不需要查看当前表的主键字段叫id sid 还是 pid了
    """

    # user_obj = models.User.objects.filter(pk=8).first()
    # res = user_obj.delete()
    # print(res)  # ==> (1, {'app03.User': 1})

    "改"
    # models.User.objects.filter(pk=9).update(name='vivi')

    # user_obj = models.User.objects.get(pk=10)
    # user_obj.name = 'tom'
    # user_obj.save()
    # print(user_obj)  # ===> User object (9)
    """
        get 方法返回的直接就是当前数据对象
        但是该方法不推荐使用 
            一旦数据不存在该方法会直接报错  而 filter 则不会 所以推荐使用 filter
    """

    "查"
    # res = models.User.objects.all()           # 1.查全部
    # res = models.User.objects.filter(pk=1)    # 2.按照条件查询数据的某些字段值
    # res = models.User.objects.get(pk=1)       # 3.直接拿数据对象 不存在报错
    res = models.User.objects.first()         # 4.查第一个
    # res = models.User.objects.last()          # 5.查最后一个

    # res = models.User.objects.values('name', 'age')        # 6.查询表中某些字段的值     可以看成是列表套字典
    # res1 = models.User.objects.values_list('name', 'age')  # 7.查询表中某些字段的值  可以看成是列表套元组
    # res = models.User.objects.values('name', 'age').distinct()  # 8.去重

    # res = models.User.objects.order_by('age')   # 9.按年龄升序
    # res = models.User.objects.order_by('-age')  #   按年龄降序

    # res = models.User.objects.order_by('age').reverse()  # 10.将有序数据反转
    # res = models.User.objects.filter(age=18).count()     # 11.统计当前数据条数
    # res = models.User.objects.exclude(name='jason')      # 12.查询排除某一条件外的所有数据
    # res = models.User.objects.filter(pk=2).exists()  # 13.数据存放返回True否则返回False

    # res = models.User.objects.filter(pk=1).values('name', 'age')
    res1 = models.User.objects.filter(pk=1).values_list('name', 'age')

    print(res)

    "双下划线查询"
    # 年龄大于/小于35岁的数据
    # res = models.User.objects.filter(age__gt=35)  # 大于
    # res = models.User.objects.filter(age__lt=35)  # 小于

    # 大于等于/小于等于
    # res = models.User.objects.filter(age__gte=25)  # 大于等于
    # res = models.User.objects.filter(age__lte=18)  # 小于等于

    # 年龄是 17 18 25
    # res = models.User.objects.filter(age__in=[17, 18, 25])

    # 年龄在 17 到 30 之间的 收尾都要
    # res = models.User.objects.filter(age__range=[17, 30])  # 17 <= x <= 30 左右都包含

    # 查询名字中包含t 的数据  模糊查询
    # res = models.User.objects.filter(name__contains='t')   # 字母区分大小写
    # res = models.User.objects.filter(name__icontains='t')  # 字母不区分大小写

    # 查询注册时间是 2021 11月
    # res = models.User.objects.filter(register_time__month='11')
    # res = models.User.objects.filter(register_time__month='5', register_time__year='2020')

    # print(res)


if __name__ == '__main__':
    main()
