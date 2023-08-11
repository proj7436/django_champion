from django.urls import path
from .views import Main, AdminSite, ranking_view


urlpatterns = [
    path('view', ranking_view, name='víe'),
    path('champion', Main.as_view(), name='main'),
    path('admin06', AdminSite.as_view(), name='admin')
]