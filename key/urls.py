from django.shortcuts import redirect
from django.urls import path
from .views import ChangeKey, ShowKey, KeyAPI, ChangeSourceCode, APISourceCode


app_name = 'Key'

urlpatterns = [
    path('show_key/<str:pass_class_key>', ShowKey.as_view(), name='show_key'),
    path('KeyAPI/<str:pass_class_key>', KeyAPI.as_view(), name='key_api'),
    path('ChangeKey/', ChangeKey.as_view(), name='change_key'),
    path('get_source_code', APISourceCode.as_view(), name='get_code'),
    path('change_source_code', ChangeSourceCode.as_view(), name='change_code' )
]
