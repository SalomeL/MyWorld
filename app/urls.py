from django.urls import path
from app import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'hello/', views.hello),
    path(r'home/', views.home, name='home'),
]
