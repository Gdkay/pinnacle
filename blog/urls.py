from django.urls import path, include
from . import views


urlpatterns = [
    #for 127.0.0.1:8000-->local
    #pinnacle.com --> online
    path('', views.post_list, name='post_list'),

    #for 127.0.0.1:8000/post/1 --> local
    #pinnacle.com/post/1 --> online
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    #for 127.0.0.1:8000/post/new --> local
    #pinnacle.com/post/new --> online
    path('post/new', views.post_new, name='post_new'),

    #for 127.0.0.1:8000/post/1/edit --> local
    #pinnacle.com/post/1/edit --> online
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),

    #for 127.0.0.1:8000/post/1/delete --> local
    #pinnacle.com/post/1/delete --> online
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),

    #for 127.0.0.1:8000/drafts --> local
    #pinnacle.com/drafts --> online
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    #for 127.0.0.1:8000/post/1/publish --> local
    #pinnacle.com/post/1/publish --> online
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),

    #for 127.0.0.1:8000/post/1/comment --> local
    #pinnacle.com/post/1/comment --> online
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),

    # for 127.0.0.1:8000/comment/1/remove --> local
    # pinnacle.com/post/comment/1/remove --> online
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    # for 127.0.0.1:8000/comment/1/approve --> local
    # pinnacle.com/post/comment/1/approve --> online
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),

]