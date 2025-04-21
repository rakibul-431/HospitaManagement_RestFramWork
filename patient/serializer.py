from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
class PatientViewSet(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Patient
        fields='__all__'


class RejistrationSerializer(serializers.ModelSerializer):
    conform_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','conform_password']
    
    def save(self):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        password=self.validated_data['password']
        password2=self.validated_data['conform_password']

        if password != password2:
            raise serializers.ValidationError({'error':"Passord doesn't exists"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email already Exists"})
        account=User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password)
        account.is_active=False
        account.save()
        return account

class Userloginserializer(serializers.ModelSerializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    # class Meta:
    #    field=['username','password']