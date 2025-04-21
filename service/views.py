from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .import serializer
# Create your views here.
class ServiceViewset(viewsets.ModelViewSet):
    queryset=models.Service.objects.all()
    serializer_class=serializer.ServiceViewSet
