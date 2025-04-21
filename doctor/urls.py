from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()

router.register('list',views.DoctorView_set)
router.register('Designation',views.DesignationView_set)
router.register('Specialization',views.SpecializationView_set)
router.register('Available',views.AvailableTimeView_set)
router.register('reviewlist',views.ReviewView_set)

urlpatterns = [
    path('',include(router.urls))
]

