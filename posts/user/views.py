from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth import login
from .models import RegistrationForm

# Create your views here.
def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('post_list')
    return render(request, 'register_user.html', {'form': form})