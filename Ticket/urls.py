from django.urls import path
from .views import book,all,markAsClosed,query,delete
urlpatterns = [
    path('new/',book),
    path('all/',all),
    path('markAsClosed/',markAsClosed),
    path('delete/',delete),
    path('<str:search>/',query),
]