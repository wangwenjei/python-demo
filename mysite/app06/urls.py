from django.urls import path
from app06 import views  # 研究cookie与session方法的使用
from app06 import middlemare_views  # 研究自定义中间件
from app06 import notify_views  # 研究利用 importlib 模块实现配置热插拔
from app06 import auth_views  # 研究auth模块使用

urlpatterns = [
    # cookie方式实现登录验证
    path(r'login/', views.login),
    path(r'home/', views.home),
    path(r'index/', views.index),
    path(r'logout/', views.logout),

    # session方式实现登录验证
    path(r'mylogin/', views.MyLogin.as_view()),
    path(r'myhome/', views.MyHome.as_view()),
    path(r'myindex/', views.MyIndex.as_view()),
    path(r'mylogout/', views.MyLogout.as_view()),

    path(r'set_session/', views.set_session),
    path(r'get_session/', views.get_session),


    path(r'mydd_index/', middlemare_views.index),
    path(r'csrf/', middlemare_views.csrf),
    path(r'mycsrf/', middlemare_views.MyCsrf.as_view()),

    path(r'notify/', notify_views.Notify.as_view()),


    # 研究auth相关内容
    path(r'auth_login/', auth_views.auth_login),
    path(r'auth_home/', auth_views.auth_home),
    path(r'auth_set_password/', auth_views.auth_set_password),
    path(r'auth_logout/', auth_views.auth_logout),
    path(r'auth_register/', auth_views.auth_register),
]