from django.contrib import admin
from .models import ContactUs

class ContactModeladmin(admin.ModelAdmin):
    list_display=['id','name','phone','problem']
 

# Register your models here.
admin.site.register(ContactUs,ContactModeladmin)
