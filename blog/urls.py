from django.urls import path
from . import views

urlpatterns = [
    #for 127.0.0.1:8000-->local
    #pinnacle.com --> online
    path('', views.post_list, name='post_list'),

    #for 127.0.0.1:8000/post/1 --> local
    #pinnacle.com --> online
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]