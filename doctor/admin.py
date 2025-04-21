from django.contrib import admin
from .models import Designations,Specialization,AvailAbleTime,Doctor,Review
# Register your models here.
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("Name",)}
class specializationsAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("Name",)}
admin.site.register(Designations,DesignationAdmin)
admin.site.register(Specialization,specializationsAdmin)
admin.site.register(AvailAbleTime)
admin.site.register(Doctor)
admin.site.register(Review)