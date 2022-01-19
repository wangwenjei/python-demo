# Generated by Django 3.2.7 on 2021-11-29 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0007_auto_20211129_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者名称')),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('addr', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社名称')),
                ('addr', models.CharField(max_length=32, verbose_name='地址')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='书名')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('publish_date', models.DateField(auto_now_add=True, verbose_name='发版日期')),
                ('authors', models.ManyToManyField(to='app03.Author')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app03.publish')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='author_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app03.authordetail'),
        ),
    ]
