from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET','POST'))
def Home(request):
    dictionary={
        "users/new":"register user",
        "tickets/new":"create ticket",
        "tickets/markasclosed":"mark as closed",
        "tickets/delete":"delet ticket",
        "api/token/":"Token genration",
        "api/token/refresh/":"Refresh token",
        "api/token/verify/":"Verify tokwn",
    }
    return Response(dictionary)