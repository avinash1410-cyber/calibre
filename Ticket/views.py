from Ticket.serializers import TickeSerializers
# Create your views here.
from .models import Customer, Ticket
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.response import Response

@api_view(('GET','POST'))
def book(request):
    if request.method == "POST":
        title = request.data['title']
        description = request.data['description']
        employee=request.data['employee']
        user = User.objects.get(username=employee)
        cust=Customer.objects.get(user=user)
        if request.user.is_staff==False:
            return Response({"Response":"You are not an admin"})
        ticket=Ticket.objects.create(title=title,description=description,assignedTo=cust)
        return Response({"message":ticket.id})
    return Response({"title":"","description":"","employee":""})



@api_view(('GET','POST'))
def query(request,search=None):
    if request.method == "POST":
        if search==None or search=="all":
            tickets=Ticket.objects.all()
            srlzr=TickeSerializers(tickets,many=True)
            return Response(srlzr.data)
        else:
            tickets=Ticket.objects.filter(Q(status__icontains=search)|
                              Q(title__icontains=search) |
                              Q(priority__icontains=search)
                              )
            srlzr=TickeSerializers(tickets,many=True)
            return Response(srlzr.data)
    return Response({"search":""})



@api_view(('GET','POST'))
def all(request):
    tickets=Ticket.objects.all()
    srlzr=TickeSerializers(tickets,many=True)
    return Response(srlzr.data)

@api_view(('GET','POST'))
def markAsClosed(request):
    if request.method == "POST":
        ticketId = int(request.data['ticketId'])
        ticket=Ticket.objects.get(id=ticketId)
        cpr=ticket.priority
        cust=Customer.objects.get(user=request.user)
        userticket=Ticket.objects.filter(assignedTo=cust)
        for ticket in userticket:
            if ((cpr=="Low" and ticket.priority=="Medium") or (cpr=="Low" and ticket.priority=="High")or(cpr=="Medium" and ticket.priority=="High")):
                return Response({"Response":"u have assign a more priority already"})
        if request.user==ticket.assignedTo.user or request.user.is_staff:
            ticket.status="close"
            ticket.save()
            return Response({"message":ticket.id})
        else:
            return Response({"msg":"U are not authorized"})
    return Response({"ticketId":""})



@api_view(('GET','POST'))
def delete(request):
    if request.method == "POST":
        ticketId = request.data['ticketId']
        ticket=Ticket.objects.get(id=ticketId)
        if ticket==None:
            return Response({"msg":"No ticket Found"})
        if request.user.is_staff:
            ticket.delete()
        else:
            return Response({"msg":"U are not authorized"})
        return Response({"message":"Deleted"})
    return Response({"ticketId":""})