from django.urls import path
from .views import Main, AdminSite

  
app_name = 'champion'


urlpatterns = [
    path('champion', Main.as_view(), name='main'),
    path('admin06', AdminSite.as_view(), name='admin')
]