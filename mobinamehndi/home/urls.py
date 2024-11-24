from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView, )

urlpatterns = [
    # Template URLs
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('service/', views.service, name = "service"),
    path('product/', views.product, name = "product"),
    path('test/', views.test, name = "test"),

    # Authentication URLs
    path('api/register/', views.registerView, name='api_register'),
    path('api/login/', views.loginView, name='api_login'),
    path('api/logout/', views.loginView, name='api_logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Product URLs
    path('api/products/', views.getProductView, name='get_products'),
    path('api/products/create', views.postProductView, name='post_products'),

]
