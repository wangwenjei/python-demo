from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app03 import models

    " 在为choice相关字段存值时,没有列举出来的选项也可以存储,存储的范围还是按照字段类型决定 "
    # models.Admin_User.objects.create(username='jason', age=18, gender=1, score='A')
    # models.Admin_User.objects.create(username='vivi', age=18, gender=2, score='A')
    # models.Admin_User.objects.create(username='tom', age=18, gender=3, score='D')
    # models.Admin_User.objects.create(username='jack', age=18, gender=4, score='C')

    """
        1.只要是choice参数的字段,如果你想要获取对应的信息,需要使用固定写法 get_字段名_display()
        2.如果没有对应关系,那么字段存的是什么就还展示什么
    """
    user_obj = models.Admin_User.objects.filter(pk=1).first()
    print(user_obj.get_gender_display())

    user_obj = models.Admin_User.objects.filter(pk=4).first()
    print(user_obj.get_gender_display())


if __name__ == '__main__':
    main()
