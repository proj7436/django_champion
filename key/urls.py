from django.shortcuts import redirect
from django.urls import path
from .views import ShowKey, KeyAPI




urlpatterns = [
    path('show_key/<str:pass_class_key>', ShowKey.as_view(), name='show_key'),
    path('KeyAPI/<str:pass_class_key>', KeyAPI.as_view(), name='key_api'),
]
