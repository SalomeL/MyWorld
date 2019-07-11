from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def nomy(request):
    return render(request, 'nomy/index.html')


def home(request):
    return render(request, 'home/home.html')


def login(request):
    return render(request, 'home/login.html')
