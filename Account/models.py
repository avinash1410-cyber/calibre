from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.user.username