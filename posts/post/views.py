from django.shortcuts import render
from django.http import HttpResponse
from .models import PostForm

# Create your views here.
def post_form(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'post_form.html', {'form': form})