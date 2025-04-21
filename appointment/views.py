from django.shortcuts import render
from . import serializer
from rest_framework import viewsets
from . import models

# Create your views here.
class AppointmentView_Set(viewsets.ModelViewSet):
    queryset=models.Appointment.objects.all()
    serializer_class=serializer.AppointmentViewSet

    # def get_queryset(self):
    #     queryset=super().get_queryset() #7 number line ke niye aslam / parent ke niye aslam
    #     patient_id=self.request.query_params.get('patient_id')
    #     if patient_id:
    #         queryset=queryset.filter(patient_id=patient_id)
    #     return queryset