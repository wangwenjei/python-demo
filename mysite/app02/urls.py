from django.contrib import admin
from django.urls import path
from django.conf.urls import url  # url方式添加路由 Django3.0 中默认是path方式
from django.views import View  # CBV路由匹配

from app02 import views
from app02 import template_views

urlpatterns = [
    # FBV路由
    path('roule001/', views.roule001),

    # CBV路由
    path('MyLogin/', views.MyLogin.as_view()),
    path('UploadFile/', views.UploadFile.as_view()),

    # 模板语法传值_过滤器_标签
    path('t_table/', template_views.index),

    # 模板继承demo
    path('t_home/', template_views.home),
    path('t_login/', template_views.login),
    path('t_reg/', template_views.register),

]
