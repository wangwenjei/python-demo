from django.shortcuts import render, HttpResponse, redirect
from django.views import View

"""
    模板继承 主要是前端写法
"""


def index(request):
    n = 123
    f = 11.11
    s = '模板语法传值知识点'
    b = True
    l = ['jason', 'vivi', 'tom', 'mary']
    t = (111, 222, 333)
    d = {'username': 'jaosn', 'age': 18, 'info': '这个人有点东西'}
    se = {'夏', '商', '周'}




    return render(request, 'app02/模板传值.html', locals())




def home(request):
    return render(request, 'app02/template_views/t_home.html')


def login(request):
    return render(request, 'app02/template_views/t_login.html')


def register(request):
    return render(request, 'app02/template_views/t_register.html')
