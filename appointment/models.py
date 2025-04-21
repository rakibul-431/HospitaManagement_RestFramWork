from django.db import models
from doctor.models import Doctor,AvailAbleTime
from patient.models import Patient

# Create your models here.
AppointmentStatus=[
    ('Completed','Completed'),
    ('running','running'),
    ('pending','pending'),
]
AppointmentType=[
    ('online','online'),
    ('offline','offline'),
]
class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_type=models.CharField(choices=AppointmentType,max_length=10)
    appointment_status=models.CharField(choices=AppointmentStatus,max_length=10,default='pending')
    symtomp=models.TextField()
    time=models.ForeignKey(AvailAbleTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f'Doctor: {self.doctor.user.first_name}  patient: {self.patient.user.first_name}'


