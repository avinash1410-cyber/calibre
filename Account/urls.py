from django.urls import path
from .views import register_page
urlpatterns = [
    path('new/', register_page),
    ]