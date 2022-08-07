from http.client import HTTPResponse
from .models import Customer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token




@api_view(('GET','POST'))
def register_page(request):
    if request.method == "POST":
        userName = request.data['username']
        userPass = request.data['password']
        role=request.data['role']
        user = User.objects.create_user(userName,None, userPass)
        if role=='admin':
            user.is_staff=True 
            user.save()
        cust=Customer.objects.create(
            user=user,
            role=role,
        )
        token = Token.objects.create(user=user)
        return Response({"Token":token.key})
    return Response({"username":"","password":"","role":""})


@api_view(('GET','POST'))
def getToken(request):
    if request.method == "POST":
        userName = request.data['username']
        user = User.objects.get(username=userName)
        token = Token.objects.create(user=user)
        return Response({"Token":token.key})
    return Response({"username":""})