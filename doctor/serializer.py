from rest_framework import serializers
from . import models

class DoctorViewSet(serializers.ModelSerializer):
    # user=serializers.StringRelatedField(many=False)
    # specialization=serializers.StringRelatedField(many=True)
    # designations=serializers.StringRelatedField(many=True)
    # availabletime=serializers.StringRelatedField(many=True)
    class Meta:
        model=models.Doctor
        fields='__all__'
class SpecializationViewSet(serializers.ModelSerializer):
    class Meta:
        model=models.Specialization
        fields='__all__'
class DesignationViewSet(serializers.ModelSerializer):
    class Meta:
        model=models.Designations
        fields='__all__'
class AvailableTimeViewSet(serializers.ModelSerializer):
    class Meta:
        model=models.AvailAbleTime
        fields='__all__'

class ReviewViewSet(serializers.ModelSerializer):
    reviewr=serializers.StringRelatedField(many=False)
    doctor=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Review
        fields='__all__'