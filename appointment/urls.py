from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('appointment',views.AppointmentView_Set)

urlpatterns = [
    path('',include(router.urls))
]
