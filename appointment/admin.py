from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class appointmentAdmin(admin.ModelAdmin):
    list_display=['doctor','patient','appointment_type','appointment_status','symtomp','time','cancel']

    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
    def save_model(self, request, obj, form, change):
        if obj.appointment_status=='Running' and obj.appointment_type=='online':
            email_subject="Your online appointment is Running"
            email_body=render_to_string('admin_permission.html',{'user':obj.patient.user,'doctor':obj.doctor})
            email=EmailMultiAlternatives(email_subject,'',to=[obj.patiend.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()  
        return super().save_model(request, obj, form, change)

admin.site.register(Appointment,appointmentAdmin)

# Register your models here.
