from .models import Customer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


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
        token=get_tokens_for_user(user)
        return Response({"":token})
    return Response({"username":"","password":"","role":""})