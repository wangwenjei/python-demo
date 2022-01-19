from django.shortcuts import render, HttpResponse, redirect
from app04 import models


# Create your views here.

def home(request):
    return render(request, 'app04/home.html')


def book_list(request):
    # 从数据库获取书籍
    book_queryset = models.Book.objects.all()

    return render(request, 'app04/book_list.html', locals())


def book_add(request):
    """
        添加书籍接口
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 获取前端提交的数据
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish_date = request.POST.get("publish_date")
        publish_id = request.POST.get("publish")
        authors = request.POST.getlist("authors")  # [1,2,3,]

        # 数据存储
        # 书籍表添加数据
        book_obj = models.Book.objects.create(title=title, price=price, publish_date=publish_date,
                                              publish_id=publish_id)
        # 书籍作者关系表添加数据,将authos获取到的作者列表打散添加
        book_obj.authors.add(*authors)

        """
            redirect括号内可以直接写URL,也可以直接写别名
            但是如果你的别名需要添加额外的参数的话,就必须要使用reverse解析
        """
        return redirect('app04_book_list')

    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'app04/book_add.html', locals())


def book_edit(request, edit_id):
    book_queryset = models.Book.objects.filter(pk=edit_id).first()

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')

        # 数据存储
        # 修改书籍表数据
        models.Book.objects.filter(pk=edit_id).update(title=title, price=price, publish_date=publish_date,
                                                      publish_id=publish_id)
        # 修改书籍作者关系表
        book_queryset.authors.set(authors_list)
        return redirect('app04_book_list')

    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    return render(request, 'app04/book_edit.html', locals())


def book_delete(request, delete_id):
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('app04_book_list')
