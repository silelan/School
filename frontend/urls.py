
from django.urls import path
from .views import *

app_name = "frontend"

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('admission/', AdmissionView.as_view(), name='admission'),
    path('gallery/',GalleryView.as_view(), name='gallery'),
    path('achivements/',AchivementsView.as_view(), name='achivements'),
    path('about/', AboutView.as_view(), name='about'),
    path('history/', HistoryView.as_view(), name='history'),
    path('career/', CareerView.as_view(), name='career'),   
    path('event/', EventView.as_view(), name='event'),   
    path('blog/', BlogView.as_view(), name='blog'),    
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
    
]
