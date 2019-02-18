from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogPageView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'blog'

class DetailBlogPageView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'