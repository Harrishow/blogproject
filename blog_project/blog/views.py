from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_details(request):
    post = Post.objects.all()
    return render(request, 'blog/post_details.html', {'post': post})

def login(request):
    post = Post.objects.all()
    return render(request, 'login/login.html', {'post' : post})
