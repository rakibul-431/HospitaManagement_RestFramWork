from django.urls import path,include
from service import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('service',views.ServiceViewset)

urlpatterns = [
    path('',include(router.urls)),
]
