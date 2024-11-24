from django.shortcuts import render
from rest_framework import decorators as rest_decorators , status
from rest_framework.response import Response
# from .serializers import ProductSerializer
# from .models import ProductModel
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

def test(request):
    return render(request, "test.html")

"""Product API"""

#GET
# @rest_decorators.api_view(["GET"])
# @rest_decorators.permission_classes([])
# def getProductView(request):
#     try:
#         #retriving data from ProductModel
#         data = ProductModel.objects.all()
#         #serialize the data using ProductSerializer
#         serialize_data = ProductSerializer(data, many = True)
#         if serialize_data:
#             return Response({"data": serialize_data}, status=status.HTTP_200_OK)
#         return Response({"error": "error"})
#     except Exception as e:
#         return Response({"error": str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

# #POST
# @rest_decorators.api_view(["POST"])
# @rest_decorators.permission_classes([])
# def postProductView(request):
#     try:
#         #converting the data into serializert format
#         serialize_data = ProductSerializer(data = request.data)
#         #checking for data is valid or not and raising error
#         serialize_data.is_valid(raise_exception = True)
#         product = serialize_data.save()
#         if product is not None:
#             return Response("Product Inserted")
#     except Exception as e:
#         return Response({"error": str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

