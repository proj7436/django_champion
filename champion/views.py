from django.shortcuts import render
from django.views import View
from .models import Champion
# Create your views here.


class Main(View):
    def get(self, request):
        return render(request, 'main.html')
    



class AdminSite(View):
    def get(self, request):

        oj = Champion.objects.all()
        return render(request, 'admin.html', {"list":oj})