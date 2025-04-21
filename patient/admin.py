from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display=['first_name','mobile_number','image']

    def first_name(self,obj):
        return obj.user.first_name
        

# Register your models here.

admin.site.register(Patient,PatientAdmin)
