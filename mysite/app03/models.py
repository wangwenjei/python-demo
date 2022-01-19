from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    register_time = models.DateField()
    """
    DateField   记录 年月日
    DateTimeField  记录 年月日时分秒
        两个重要参数
            auto_now: 每次操作数据的时候, 该字段会自动将当前时间更新
            auto_now_add: 在创建数据的时候会自动将当前创建时间记录下来, 之后只要不人为修改数据那么将一直不变
    """

    def __str__(self):
        return 'obj_name:%s' % self.name


# 书籍表
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
    publish_date = models.DateField(auto_now_add=True, verbose_name='发版日期')
    book_sold = models.IntegerField(default=1000, verbose_name='售出书籍')
    book_inventory = models.IntegerField(default=300, verbose_name='库存书籍')

    # 一对多/多对一
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    # 多对多
    authors = models.ManyToManyField(to='Author')


# 出版社表
class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社名称')
    addr = models.CharField(max_length=32, verbose_name='地址')
    email = models.EmailField()

    def __str__(self):
        return '对象: %s' % self.name


# 作者表
class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name='作者姓名')
    age = models.IntegerField()

    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


# 作者详情表  python3 manage.py makemigrations  python3 manage.py migrate
class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


# choices参数demo
class Admin_User(models.Model):
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他'),
    )
    score_choices = (
        ('A', '优秀'),
        ('B', '良好'),
        ('C', '及格'),
        ('D', '不及格'),
    )

    username = models.CharField(max_length=32, verbose_name='用户名')
    age = models.IntegerField(verbose_name='年龄')
    # 保证字段类型跟列举出来的元祖第一个数据类型一致即可
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别')
    score = models.CharField(choices=score_choices, max_length=32, null=True, verbose_name='成绩等级')

    """
        1.gender字段存储的依旧还是数字,但是如果存储的数字在对应的choices列举的范围内,就可以非常轻松的获取到与数字相对应的真正的值
        2.gender字段在存入值时,存储的数字不在choices字段的列举范围内依旧可以存入,存入的限制是字段做限制的
        3.在取值时,使用get_字段名_display可以获取到数值对应的choices的值,如果choices内没有对应的值则存入什么值就展示什么值
    """
