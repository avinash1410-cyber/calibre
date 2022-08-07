from django.db import models
from Account.models import Customer

class Ticket(models.Model):
    Status = (
        ("open", "open"),
        ("close", "close"),
    )
    Priority = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High","High"),
    )
    description=models.CharField(max_length=300,blank=True,null=True)
    title=models.CharField(max_length=30,blank=True,null=True)
    priority=models.CharField(max_length=20,default="Low",choices=Priority, null=True)
    assignedTo=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    createdAt=models.DateField(auto_now_add=True)
    status= models.CharField(max_length=20,default="open",choices=Status, null=True)

    def __str__(self):
        return str(self.title)