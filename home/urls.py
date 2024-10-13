from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('service/', views.service, name = "service"),
    path('product/', views.product, name = "product"),

]
