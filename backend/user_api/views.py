import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth import login, authenticate, logout

from .models import Account
from .serializers import (
    AccountRegisterSerializer,
    UserSerializer,
)

# user list
@api_view(['GET'])
def user_list_api(request):
    accounts = Account.objects.all()
    serializer = UserSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_register_api(request):
    if request.method == 'POST':
        serializer = AccountRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully Your Account created.'
            data['username'] = user.username
            data['email'] = user.email
        else:
            data = serializer.errors
        return Response(data)

@api_view(['POST'])
def user_login_api(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    data = {}
    if user is not None:
        login(request, user)
        data['response'] = 'Successfully Login.'
        print(data)
        return Response(data)
    

@api_view(['GET'])
def api_view(request):
    data = {
        'api/',
    }
    return Response(data)