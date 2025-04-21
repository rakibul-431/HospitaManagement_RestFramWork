from django.shortcuts import render
from rest_framework import viewsets,pagination
from . import models,serializer
# Create your views here.

#pagination 
class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100


#doctor view set
class DoctorView_set(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serializer.DoctorViewSet
    pagination_class=DoctorPagination

class DesignationView_set(viewsets.ModelViewSet):
    queryset=models.Designations.objects.all()
    serializer_class=serializer.DesignationViewSet

class SpecializationView_set(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serializer.SpecializationViewSet

class AvailableTimeView_set(viewsets.ModelViewSet):
    queryset=models.AvailAbleTime.objects.all()
    serializer_class=serializer.AvailableTimeViewSet

class ReviewView_set(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializer.ReviewViewSet
