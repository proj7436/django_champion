from django.urls import path
from .views import Main


urlpatterns = [
    path('champion', Main.as_views(), name='main')
]