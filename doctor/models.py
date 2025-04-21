from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.
class Specialization(models.Model):
    Name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40)
    def __str__(self):
        return self.Name

class Designations(models.Model):
    Name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40)

    def __str__(self):
        return self.Name

class AvailAbleTime(models.Model):
    Name=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
class Doctor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="doctor/images/")
    designations=models.ManyToManyField(Designations)
    specialization=models.ManyToManyField(Specialization)
    availabletime=models.ManyToManyField(AvailAbleTime)
    fee=models.IntegerField()
    meet_link=models.CharField(max_length=100)

    def __str__(self):
        return f'Dr.{self.user.first_name} {self.user.last_name}'
STAR_CHOICES=[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewr=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body=models.TextField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICES,max_length=10)

    def __str__(self):
        return f'Patient:{self.reviewr.user.first_name} Doctor:{self.doctor.user.first_name}'




