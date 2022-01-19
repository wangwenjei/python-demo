from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app03 import models

    "  聚合查询  "
    """
        只要是跟数据库有关的模块基本上都在django.db.models里面,如果没有还有可能在django.db里
        聚合函数通常情况下都是配合分组一起使用
        单独使用聚合函数需要使用关键字aggregate
        
    """
    # from django.db.models import Max, Min, Sum, Count, Avg
    # res = models.Book.objects.aggregate(Max('price'), Min('price'), Sum('price'), Count('pk'), Avg('price'))
    # print(res)

    "  分组查询  "
    from django.db.models import Max, Min, Sum, Count, Avg
    # 1.统计每一本书的作者个数
    # res = models.Book.objects.annotate(author_num=Count('authors')).values('title', 'author_num')
    # print(res)
    """
    # 原生SQL写法
        --  SELECT 
        -- 	    app03_book.title,
        -- 	    COUNT( app03_book_authors.author_id ) AS author_num
        --  FROM
        -- 	    app03_book
        -- 	LEFT JOIN app03_book_authors ON app03_book.id = app03_book_authors.book_id
        --      GROUP BY
        -- 	app03_book.id
        
    """

    # 2.统计每个出版社卖的最便宜的书的价格
    # res = models.Publish.objects.annotate(min_price=Min('book__price')).values('name', 'min_price').query
    # print(res)
    """
    # 原生SQL写法
        --  SELECT
        -- 	    app03_publish.name,
        -- 	    MIN( app03_book.price ) AS price 
        --  FROM
        -- 	    app03_publish
        -- 	    LEFT JOIN app03_book ON app03_publish.id = app03_book.publish_id
        --  GROUP BY
        -- 	    app03_publish.id

    """

    # 3.统计不止一个作者的图书
    """
        1.先按照图书分组, 求每一本书的对应作者数
        2.过滤出不止一个作者的图书
    """
    # res = models.Book.objects.annotate(author_num=Count('authors')).filter(author_num__gt=1).values('title',
    #                                                                                                 'author_num').query
    # print(res)
    """
    # 原生SQL写法
        --  SELECT
        -- 	    app03_book.title,
        -- 	    COUNT(app03_book_authors.author_id) AS author_num
        --  FROM
        -- 	    app03_book
        -- 	    LEFT JOIN app03_book_authors ON app03_book.id = app03_book_authors.book_id
        --  GROUP BY
        -- 	    app03_book.id
        --  HAVING
        -- 	    COUNT(app03_book_authors.author_id) > 1

    """

    # 4.查询每个作者出的书的总价格
    # res = models.Author.objects.annotate(sum_price=Sum('book__price')).values('name', 'sum_price')
    # print(res)
    """
    # 原生SQL写法
        --  SELECT
        -- 	    app03_author.`name`,
        -- 	    SUM( app03_book.price ) AS price_sum 
        --  FROM
        -- 	    app03_author
        -- 	    LEFT JOIN app03_book_authors ON app03_author.id = app03_book_authors.author_id
        -- 	    LEFT JOIN app03_book ON  app03_book_authors.author_id = app03_book.id 
        --  GROUP BY
        -- 	    app03_author.id

    """

    "  F 与 Q 查询"
    # F查询
    """  弄够帮助你直接获取到表中某个字段对应的数据 """
    from django.db.models import F

    # 1.查询卖出数大于库存数的书籍
    # res = models.Book.objects.filter(book_sold__gt=F('book_inventory')).values('title')
    # print(res)

    # 2.将所有书籍的价格提升500块
    # models.Book.objects.update(price=F('price') + 500)

    # 3.将所有书的名称后面加上爆款两个字   在操作字符类型的数据的时候 F不能够直接做到字符串的拼接
    """ 在操作字符串类型的数据时,F不能够直接做到字符串的拼接需要用到Concat方法,直接拼接会直接为空 """
    # from django.db.models.functions import Concat
    # from django.db.models import Value

    # models.Book.objects.update(title=Concat(F('title'), Value('爆款')))
    """
        # 删除列中爆款字符
        -- UPDATE app03_book SET title = REPLACE(title,'爆款','')
    """

    # Q查询
    """ filter括号内多个参数是AND关系, 用Q可以让filter可以使用AND,OR,NOT关系,高阶用法还可以将查询条件的左边也变为字符串的形式 """
    # 1.查询卖出数大于100或者价格小于600的书籍
    # res = models.Book.objects.filter(book_sold__gt=100, price__lt=600).values('title')
    # print(res)

    from django.db.models import Q
    # res = models.Book.objects.filter(Q(book_sold__gt=100), Q(price__lt=600)).values('title')     # 卖出>100 AND 价格<600
    # res = models.Book.objects.filter(Q(book_sold__gt=100) | Q(price__lt=600)).values('title')    # 卖出>100 OR  价格<600
    # res = models.Book.objects.filter(~Q(book_sold__gt=100) | ~Q(price__lt=600)).values('title')  # 卖出<=100 OR  价格>=600
    # print(res)

    " Q高阶用法 能够将查询条件的左边也变成字符串的形式"
    q = Q()
    q.connector = 'or'
    q.children.append(('book_sold__gt', 100))
    q.children.append(('price__lt', 600))
    res = models.Book.objects.filter(q).values('title')
    print(res)


if __name__ == '__main__':
    main()
