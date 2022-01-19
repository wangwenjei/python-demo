from django.urls import path

from app03 import views

urlpatterns = [
    path(r'index/', views.index)
]
