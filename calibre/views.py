from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET','POST'))
def Home(request):
    dictionary={
        "users/new":"register user",
        "tickets/new":"create ticket",
        "tickets/markasclosed":"mark as closed",
        "tickets/delete":"delet ticket",
        "users/getToken":"get token for user"
    }
    return Response(dictionary)