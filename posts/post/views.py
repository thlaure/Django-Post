from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostForm, Post

# Create your views here.
def post_form(request):
    if (not request.user.is_authenticated):
        return redirect('login')

    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'post_form.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})