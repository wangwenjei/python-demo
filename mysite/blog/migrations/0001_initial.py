# Generated by Django 3.2.7 on 2021-12-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='用户名')),
                ('password', models.CharField(default='123456', max_length=256, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='用户注册时间')),
                ('isuser', models.BooleanField(default='False', verbose_name='用户是否被删除 1:未删除 0:删除')),
            ],
        ),
    ]
