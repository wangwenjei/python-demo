from django.db import models


# Create your models here.

class User(models.Model):
    gender_choices = (
        (1, 'male'),
        (2, 'female'),
        (3, 'others')
    )
    username = models.CharField(max_length=32, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别')


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
