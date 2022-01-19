from django.db import models


# Create your models here.

# 书籍表
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='价格')
    publish_date = models.DateField(auto_now_add=True, verbose_name='发版日期')

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
