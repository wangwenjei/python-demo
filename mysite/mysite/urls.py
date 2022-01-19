"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
一个应用单独路由
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index/', views.index),
    path(r'home/', views.home),
    path(r'ab_render/', views.ab_render),  # render 返回参数传值给HTML

    path('', views.home),  # 首页
    path(r'blog/', views.blog),  # 登录功能
    path(r'register/', views.reg),  # 注册功能
    path(r'userlist/', views.userlist),  # 展示用户列表
    path(r'edit_user/', views.edit_user),  # 编辑用户
    path(r'delete_user/', views.delete_user),

]

"""

"""
# 路由分发
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app01 import urls as app01_urls
from app02 import urls as app02_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # 路由分发
    url(r'app01/', include(app01_urls)), # 只要是url前缀是以app01开头的,全部交给app01处理
    url(r'app02/', include(app02_urls)),

]
"""
# 路由分发 终极写法
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 路由分发
    path(r'app01/', include('app01.urls')),  # 只要是url前缀是以app01开头的,全部交给app01处理
    url(r'app02/', include('app02.urls')),
    path(r'app03/', include('app03.urls')),
    path(r'app04/', include('app04.urls')),  # 图书管理系统Demo
    path(r'app05/', include('app05.urls')),  # Ajax相关学习
    path(r'app06/', include('app06.urls')),  # cookie session

    path(r'blog/', include('blog.urls')),  # 用户登录Demo

]
