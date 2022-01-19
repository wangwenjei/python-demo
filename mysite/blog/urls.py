from django.urls import path

from blog import views

urlpatterns = [
    path(r'login/', views.Login.as_view()),
    path(r'blog/edit/', views.BlogManagement.as_view(), name='blog_edit')
]
