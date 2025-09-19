from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model


def my_blog(request):
    return HttpResponse("Hello, blog!")


User = get_user_model()


def your_view(request):
    users = User.objects.all()
