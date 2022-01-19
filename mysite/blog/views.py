import requests
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.db.models import Q
from blog import models


# Create your views here.

def login_auth(func):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()
        if request.COOKIES.get('loginUser'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/blog/login/?next=%s' % target_url)

    return inner


class Login(View):
    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = models.UserInfo.objects.filter(name=username, is_delete=1)

        if user_obj:
            if password == user_obj[0].password:
                target_url = request.GET.get('next')
                if target_url:
                    obj = redirect(target_url)
                else:
                    obj = render(request, 'blog/home.html')
                obj.set_cookie('loginUser', username, max_age=7200)
                return obj
            else:
                return render(request, 'blog/login.html', {'login_error': '用户名或密码错误'})

        return render(request, 'blog/login.html', {'login_error': '用户名或密码错误'})


class BlogManagement(View):
    @method_decorator(login_auth)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'blog/blog_edit.html')

    def post(self, request):
        return render(request, 'blog/login.html')
