from django.urls import path
from . import views

urlpatterns = [
    path('create', views.post_form),
    path('list', views.post_list),
]