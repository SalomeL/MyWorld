from django.urls import path
from app import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'hello/', views.nomy),
    path(r'home/', views.home, name='home'),
    path(r'login/', views.login, name='login'),

]
