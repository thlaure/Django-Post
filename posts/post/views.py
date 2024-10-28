from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_form(request):
    return render(request, 'post_form.html')