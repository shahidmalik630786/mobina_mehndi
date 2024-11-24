from django.shortcuts import render
from rest_framework import decorators as rest_decorators , status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductSerializer, UserSerializer
from .models import ProductModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
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


#JWT Authentication

#Register
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([])
def registerView(request):
    '''This code allows us to register and returns a JWT Token'''
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([])
def loginView(request):
    '''This code will allows us to Login'''
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error':'Please provide username and password'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)

    if user:
        refresh =  RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username':user.username,
            'email':user.email,
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#Logout
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([IsAuthenticated])
def logoutView(request):
    '''This will allow us toLogout'''
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out'},status=status.HTTP_200_OK)
        return Response({'error': 'Refresh token is required'},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)},
                       status=status.HTTP_400_BAD_REQUEST)



#Product API

#GET
@rest_decorators.api_view(["GET"])
@rest_decorators.permission_classes([IsAuthenticated])
def getProductView(request):
    '''Get all Products'''
    try:
        data = ProductModel.objects.all()
        serializer = ProductSerializer(data, many = True)
        if serializer:
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"error": "Failed to fetch products"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({"error": str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


#POST
@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([IsAuthenticated])
def postProductView(request):
    '''Create a new Product'''
    try:
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

