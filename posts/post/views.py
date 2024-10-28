from django.shortcuts import render
from django.http import HttpResponse
from .models import PostForm, Post

# Create your views here.
def post_form(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'post_form.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})