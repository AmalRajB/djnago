from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_201_CREATED
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return Response('account created...',status=HTTP_201_CREATED)
    return Response(form.errors,status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'username':user.username ,'token': token.key},status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    data = request.user
    return Response({
        "username":data.username,
        "password":data.password
    })


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def product(request):
    productlist = [
        {'name':'samsungs25',
        'price':120000,
        'category':'moblie phone'},
         {'name':'smartwatch',
        'price':10000,
        'category':'watch'},
         {'name':'jbl12B',
        'price':20000,
        'category':'speaker'},
         {'name':'iphone 17',
        'price':100000,
        'category':'moblie phone'},
         {'name':'smartTV',
        'price':40000,
        'category':'TV'}
    ]
    return Response(productlist, status=HTTP_200_OK)



    


    
