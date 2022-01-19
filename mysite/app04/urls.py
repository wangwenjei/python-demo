from django.urls import path

from app04 import views
from django.conf.urls import url

urlpatterns = [
    path(r'', views.home, name='app04_home'),
    path(r'book/list/', views.book_list, name='app04_book_list'),
    path(r'book/add/', views.book_add, name='app04_book_add'),
    url(r'^book/edit/(?P<edit_id>\d+)/', views.book_edit, name='app04_book_edit'),
    url(r'^book/delete/(\d+)/', views.book_delete, name='app04_book_delete'),
]
