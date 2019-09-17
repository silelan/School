
from django.urls import path
from .views import *

app_name = "frontend"

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('admission/', AdmissionView.as_view(), name='admission'),
    path('gallery/',GalleryView.as_view(), name='gallery'),
    path('achivements/',AchivementsView.as_view(), name='achivements'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
    
]
