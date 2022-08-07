from django.urls import path
from .views import book,all,markAsClosed,query,delete
urlpatterns = [
    path('new/',book),
    path('all/',all),
    path('markAsClosed/',markAsClosed),
    path('<str:search>/',query),
    path('delete/',delete)
]