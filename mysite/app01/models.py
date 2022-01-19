from django.db import models


# Create your models here.
class User(models.Model):
    """
        CharField 必须指定 max_length参数
        verbose_name 该参数是所有字段都有的 用来对字段的解释

        由于一张表中必须要有一个主键字段,并且一般情况下都叫id字段
        所以ORM当你不定义主键字段的时候 ORM会自动帮你创建一个名为id的主键字段
        这意味着,后面当创建模型表的时候如果主键字段没有额外的叫法,可以忽略不写

    """
    # id int primary_kay auto_increment
    # id = models.AutoField(primary_kay=True, verbose_name='主键')
    # username varchar(32)
    username = models.CharField(max_length=32, verbose_name='用户名')
    # password int
    password = models.IntegerField(verbose_name='密码')

    def __str__(self):
        return '%s' % self.username
