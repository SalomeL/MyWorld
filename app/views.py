from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return HttpResponse('Hello Django 2.2.1')


def home(request):
    return render(request, 'home/home.html')