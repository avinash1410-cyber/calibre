from django.urls import path
from .views import register_page,getToken
urlpatterns = [
    path('new/', register_page),
    path('getToken/', getToken),
    ]