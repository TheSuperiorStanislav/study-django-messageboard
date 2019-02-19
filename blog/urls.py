from django.urls import path

from .views import (
    BlogPageView,
    DetailBlogPageView, 
    CreateBlogPageView, 
    UpdateBlogPageView, 
    DeleteBlogPageView
)


urlpatterns = [
    path('post/<int:pk>/delete',DeleteBlogPageView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit',UpdateBlogPageView.as_view(), name='post_edit'),
    path('post/new/',CreateBlogPageView.as_view(), name='post_new'),
    path('post/<int:pk>/',DetailBlogPageView.as_view(), name='post_detail'),
    path('',BlogPageView.as_view(), name='blog')
]    