import imp
from statistics import mode
from rest_framework import serializers
from .models import Ticket

class TickeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields="__all__"