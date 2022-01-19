from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app04 import models
    # # 添加准备数据
    # # 作者详情
    # models.AuthorDetail.objects.create(phone='18211111111', addr='合肥')
    # models.AuthorDetail.objects.create(phone='18311111112', addr='芜湖')
    # models.AuthorDetail.objects.create(phone='18411111113', addr='安庆')
    #
    # # 作者
    # models.Author.objects.create(name='jason', age=18, author_detail_id='1')
    # models.Author.objects.create(name='tom', age=19, author_detail_id='2')
    # models.Author.objects.create(name='vivi', age=19, author_detail_id='3')
    #
    # # 出版社
    # models.Publish.objects.create(name='北方出版社', addr='北京', email='123@163.com')
    # models.Publish.objects.create(name='南方出版社', addr='南京', email='321@163.com')
    # models.Publish.objects.create(name='人民出版社', addr='上海', email='666@163.com')

    # models.Book.objects.create(title='三国演义', price='666.56', publish_id=1)
    # models.Book.objects.create(title='红楼梦', price='555.56', publish_id=3)
    # models.Book.objects.create(title='水浒传', price='636.56', publish_id=1)
    # models.Book.objects.create(title='西游记', price='366.56', publish_id=2)
    # models.Book.objects.create(title='大学', price='366.56', publish_id=1)
    # models.Book.objects.create(title='中庸', price='356.56', publish_id=2)
    # models.Book.objects.create(title='论语', price='966.56', publish_id=3)
    # models.Book.objects.create(title='孟子', price='186.56', publish_id=2)

    "准备书籍作者关系表数据"
    # book_obj = models.Book.objects.filter(pk=1).first()
    # book_obj.authors.add(2)

    # book_obj = models.Book.objects.filter(pk=2).first()
    # author_obj = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.add(author_obj)

    # book_obj = models.Book.objects.filter(pk=3).first()
    # book_obj.authors.add(1, 3)
    #
    # book_obj = models.Book.objects.filter(pk=4).first()
    # book_obj.authors.add(2)
    #
    # book_obj = models.Book.objects.filter(pk=5).first()
    # book_obj.authors.add(3)
    #
    # book_obj = models.Book.objects.filter(pk=6).first()
    # book_obj.authors.add(1)
    #
    # book_obj = models.Book.objects.filter(pk=7).first()
    # book_obj.authors.add(3)
    #
    # book_obj = models.Book.objects.filter(pk=8).first()
    # book_obj.authors.add(1)


if __name__ == '__main__':
    main()
