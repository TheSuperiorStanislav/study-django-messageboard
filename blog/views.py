from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class CreateBlogPageView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class UpdateBlogPageView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class DeleteBlogPageView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog')