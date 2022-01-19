from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    path('roule001/', views.roule001),

    path(r'index/', views.index),
    path(r'home/', views.home),
    path(r'ab_render/', views.ab_render),  # render 返回参数传值给HTML

    path('', views.home),  # 首页
    path(r'blog/', views.login),  # 登录功能
    path(r'register/', views.reg),  # 注册功能
    path(r'userlist/', views.userlist),  # 展示用户列表
    path(r'edit_user/', views.edit_user),  # 编辑用户
    path(r'delete_user/', views.delete_user),

]
