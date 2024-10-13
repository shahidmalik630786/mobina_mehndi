from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def service(request):
    return render(request, "service.html")

def product(request):
    return render(request, "product.html")