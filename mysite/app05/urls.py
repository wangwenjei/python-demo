from django.urls import path

from app05 import views
from django.conf.urls import url

urlpatterns = [
    # Ajax 初体验
    path(r'demo1/', views.demo1, name='app04_home'),
    # 前后端数据传输编码格式研究
    path(r'ab_inde/x', views.index),
    # Ajax发送JSON格式数据
    path(r'ab_json/', views.ab_json),
    # Ajax发送文件
    path(r'ab_file/', views.ab_file),
    # 序列化相关组件
    path(r'ab_ser/', views.ab_ser),

    # sweetalert相关学习
    path(r'user/list/', views.user_list),
    path(r'user/delete/', views.user_delete),

    # 批量插入
    path(r'ab_bulk_insert/', views.ab_bulk_insert),

    # 分页器推导
    path(r'ab_paging/', views.ab_paging),
    # 调用分页器插件
    path(r'my_paging/', views.my_paging),

    # form表单
    path(r'f_form/', views.f_form),
    path(r'f_index/', views.f_index),
]
