from .models import Customer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response

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
        return Response({"message":"user created api/token/ for token genration"})
    return Response({"username":"","password":"","role":""})