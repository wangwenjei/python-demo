from django.test import TestCase

# Create your tests here.
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()

    from app03 import models
    # 添加准备数据
    # # 作者详情
    # models.AuthorDetail.objects.create(phone='18211111111', addr='合肥')
    # models.AuthorDetail.objects.create(phone='18311111111', addr='芜湖')
    # models.AuthorDetail.objects.create(phone='18411111111', addr='南京')
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

    """  一对一外键增删改查  """
    "增"
    # # 直接写实际字段ID
    # models.Book.objects.create(title='西游记', price='663.98', publish_id=1)
    # models.Book.objects.create(title='三国演义', price='665.78', publish_id=2)
    # models.Book.objects.create(title='红楼梦', price='666.97', publish_id=3)
    #
    # # 虚拟字段 放对象
    # publish_obj = models.Publish.objects.filter(pk=1).first()
    # models.Book.objects.create(title='水浒传', price='664.97', publish=publish_obj)

    "删"
    # 删除是级联删除的,删除了出版社则出版社下的书籍也会被对应删除
    # models.Publish.objects.filter(pk=3).delete()
    # models.Book.objects.filter(pk=1).delete()

    "改"
    # 方法一:
    # models.Book.objects.filter(pk=2).update(publish_id=2)

    # 方法二:
    # publish_obj = models.Publish.objects.filter(pk=3).first()
    # models.Book.objects.filter(pk=2).update(publish=publish_obj)

    """  多对多外键增删改查  """
    "首先需要获取到操作对象"
    # book_obj = models.Book.objects.filter(pk=1).first()  # 获取到书籍ID为1的对象
    # print(book_obj.authors)  #  book_obj.authors 就相当于到了第三张关系表
    #
    "增"
    # book_obj.authors.add(1, 2)  # 为书籍ID为1的书籍绑定一个主键为1和2 的作者
    #
    # author_obj = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.add(author_obj)
    """
        add 为第三张关系表添加数据
            括号内既可以传数字也可以传对象 并且都支持多个
    """
    #
    "删"
    # book_obj.authors.remove(1, 2)
    #
    # author_obj = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.remove(author_obj)
    #
    "改"  # 括号内必须是一个可迭代对象
    # book_obj.authors.set([1, 2])
    #
    # author_obj = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.set([author_obj])
    #
    "清空"
    #  在第三张关系中清空某个书籍与作者的绑定关系
    # book_obj.authors.clear()
    """
        clear 括号内不要加任何参数
    """

    """  子查询  """
    #
    """  
        子查询  
              正向查询什么时候需要加.all()
                    当你的结果可能有多个的时候就需要加.all()
                    如果是一个则直接拿到数据对象
                       eg:  book_obj.publish  获取出版社,每本书只能有一个出版社
                            book_obj.authors.all()  一本书可以有多个联合作者
                            book_obj.author_detail  每个作者与作者详情都是一一对应的
                            
              反向查询什么时候需要加_set.all()
                    当你的查询结果可以有多个时 就必须加_set.all()
                    当你的结果只有一个的时候 不需要加_set.all()
    """
    #
    "  正向查询  "
    # 1.查询书籍主键为1的出版社
    # book_obj = models.Book.objects.filter(pk=1).first()
    # print(book_obj.publish.name)  # ==> 北方出版社

    # 2.查询书籍主键为2的作者
    # book_obj = models.Book.objects.filter(pk=2).first()
    # print(book_obj.authors)  # ==> app03.Author.None
    # print(book_obj.authors.all())  # ==> <QuerySet [<Author: Author object (3)>]>

    # 3.查询作者Jason的电话号码
    # author_obj = models.Author.objects.filter(name='jason').first()
    # print(author_obj.author_detail.phone)  # ==> 18211111111

    "  反向查询  "
    # 4.查询出版社是东方出版社出版的书
    # publish_obj = models.Publish.objects.filter(name='北方出版社').first()
    # print(publish_obj.book_set.all())  # ==> <QuerySet [<Book: Book object (1)>, <Book: Book object (4)>]>

    # 5.查询作者是jason写过的书
    # author_obj = models.Author.objects.filter(name='jason').first()
    # print(author_obj.book_set.all())  # ==> <QuerySet [<Book: Book object (1)>, <Book: Book object (3)>]>

    # 6.查询手机号是18311111111
    # author_detail_obj = models.AuthorDetail.objects.filter(phone=18311111111).first()
    # print(author_detail_obj.author.name)  # ==> tom

    """  连表查询  """
    # 1.查询jason的手机号和作者姓名
    # # 正向
    # res = models.Author.objects.filter(name='jason').values('name', 'author_detail__phone')
    # print(res)
    # # 反向
    # res1 = models.AuthorDetail.objects.filter(author__name='jason').values('author__name', 'phone')
    # print(res1)

    # 2.查询书籍主键为1的书籍名称和 出版社名称
    # # 正向
    # res = models.Book.objects.filter(pk=1).values('title', 'publish__name')
    # print(res)
    # # 反向
    # res1 = models.Publish.objects.filter(book__id=1).values('book__title', 'name')
    # print(res1)

    # 3.查询书籍主键为1 的作者姓名和书籍名称
    # # 正向
    # res = models.Book.objects.filter(pk=1).values('authors__name', 'title')
    # print(res)
    # # 反向
    # res1 = models.Author.objects.filter(book__pk=1).values('name','book__title')
    # print(res1)

    # 4.查询书籍主键是1的作者的姓名和手机号
    # # 正向
    # res = models.Book.objects.filter(pk=1).values('authors__name','authors__author_detail__phone')
    # print(res)
    # # 反向
    # res1 = models.Author.objects.filter(book__pk=1).values('name','author_detail__phone')
    # print(res1)


if __name__ == '__main__':
    main()
