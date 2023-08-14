from django.urls import path
from .views import Main, AdminSite, HandleInfoMatch, HandleNoti, RemoveInfoMatch

  
app_name = 'champion'


urlpatterns = [
    path('champion', Main.as_view(), name='main'),
    path('admin06', AdminSite.as_view(), name='admin'),
    path('HandleNoti', HandleNoti.as_view(), name='HandleNoti'),
    path('HandleInfoMatch', HandleInfoMatch.as_view(), name='HandleInfoMatch'),
    path('RemoveInfoMatch', RemoveInfoMatch.as_view(), name='RemoveInfoMatch'),
    
]