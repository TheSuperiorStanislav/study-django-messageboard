from django.urls import path

from .views import BlogPageView,DetailBlogPageView

urlpatterns = [
    path('post/<int:pk>/',DetailBlogPageView.as_view(), name='post_detail'),
    path('',BlogPageView.as_view(), name='blog')
]    