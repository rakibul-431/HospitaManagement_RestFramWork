from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('patient',views.PatientView_Set)
# router.register('patient1',views.RejistrationView_set)

urlpatterns = [
    path('',include(router.urls)),
    path('rejister/',views.RejistrationView_set.as_view(),name='Rejistration'),
    path('login/',views.Loginview_set.as_view(),name='login'),
    path('logout/',views.PatientLogout.as_view(),name='Logout'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
]
