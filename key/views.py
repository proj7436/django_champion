from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Key, SourceCode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAPISerializers, PostKeySerializers, GetAPISourceCodeSerializers, PostAPISourceCodeSerializers
# Create your views here.



key_free =  '74742772568_free'
key_fee = '94827395018_fee'


class ShowKey(View):
    def get(self, request, pass_class_key):
        class_key = None
        if pass_class_key == key_free:class_key='free'
        elif pass_class_key == key_fee:class_key='fee'
        key = Key.objects.get(class_key=class_key)
        return HttpResponse(f'Your KEY: {key.key}')
        
    

class KeyAPI(APIView):
    def get(self, request, pass_class_key):
        class_key = None
        if pass_class_key == key_free:class_key='free'
        elif pass_class_key == key_fee:class_key='fee'
        key = Key.objects.get(class_key=class_key)
        my_data = GetAPISerializers(key)
        return Response(data=my_data.data, status=status.HTTP_200_OK)
    
class ChangeKey(APIView):
    def post(self, request):
        my_data = PostKeySerializers(data=request.data)

        if my_data.is_valid():

            key = my_data.data['key']
            class_key = my_data.data['class_key']
            try:
                object_in_db = Key.objects.get(class_key=class_key)
                # change if object_in_db exist
                object_in_db.key = f'{key}'
                object_in_db.save()
                return HttpResponse(f'Change Success!, [class_key: {class_key}, key: {key}]', status.HTTP_200_OK)
            # create if object_in_db not exist
            except Key.DoesNotExist:
                Key.objects.create(class_key=class_key, key=key)
                return HttpResponse(f'Create Success!, [class_key: {class_key}, key: {key}]', status.HTTP_200_OK)
        
        return HttpResponse(f'Error Type!',  status.HTTP_400_BAD_REQUEST)
    

class APISourceCode(APIView):
    def get(self, request):
        code = SourceCode.objects.get()
        data =GetAPISourceCodeSerializers(code)

        return Response(data.data, status=status.HTTP_200_OK)

            

class ChangeSourceCode(View):
    def get(self, request):
        return render(request, 'key/index.html')
    

    def post(self, request):

        key_client = request.POST.get('key')
        source_code_client = request.POST.get('source_code')
        if key_client != None:
            object_in_db = SourceCode.objects.get()

            if key_client == object_in_db.key_update:
                object_in_db.code = source_code_client
                object_in_db.save()
                return HttpResponse('Change Success')
            return HttpResponse('Sai Passwỏd')
        else:pass