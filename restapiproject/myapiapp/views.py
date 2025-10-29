from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import todoform
from.models import todolist
from .serializers import todoserializers
from django.shortcuts import get_object_or_404

@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signupfn(request):
    form = UserCreationForm(request.data)
    if form.is_valid():
        form.save()
        return Response({'message': 'User created successfully!'}, status=HTTP_200_OK)
    return Response(form.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def loginfn(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error':'please provide username and password field..'},status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username,password=password)
    if user is None:
        return Response('invalid',status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key},status=HTTP_200_OK)

    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def todocreate(request):
    form = todoform(request.POST)
    if form.is_valid():
        obj=form.save()
        return Response({'id':obj.id},status=HTTP_200_OK)
    return Response(form.errors,status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todoview(request):
    item = todolist.objects.all()
    serializer = todoserializers(item,many = True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def todoupdate(request,id):
    item = get_object_or_404(todolist,pk=id)
    form = todoform(request.data,instance=item)
    if form.is_valid():
        form.save()
        return Response('todolist updated..',status=HTTP_200_OK)
    else:
        return Response(form.errors,status=HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated]) 
def tododelete(request,id):
    try:
        item =todolist.objects.get(pk=id)
        item.delete()
        return Response('todolist deleted..',status=HTTP_200_OK)
    except item.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    
    
    




    

    
        
    
     


