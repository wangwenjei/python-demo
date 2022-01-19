from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=20, null=False, default='', verbose_name='用户名')
    password = models.CharField(max_length=256, null=False, default='123456', verbose_name='密码')
    email = models.EmailField(verbose_name='用户邮箱')
    add_time = models.DateField(auto_now_add=True, verbose_name='用户注册时间')
    is_delete = models.BooleanField(default='True', verbose_name='用户是否被删除 1:未删除 0:删除')
