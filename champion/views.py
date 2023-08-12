from django.shortcuts import render
from django.views import View
from .models import Champion
from django.http import HttpResponse
# Create your views here.




class Main(View):
    def get(self, request):
        # Lấy danh sách các đối tượng từ database và sắp xếp
        champions = Champion.objects.all().order_by('point', '-h_s')
        
        # Tạo nội dung HTML từ danh sách đã sắp xếp
        table_html = "<table>"
        for index, champion in enumerate(champions, start=1):
            table_html += f"<tr><td>{index}</td><td>{champion.name}</td><td>{champion.point}</td><td>{champion.h_s}</td></tr>"
        table_html += "</table>"
        
        # Trả về HttpResponse chứa nội dung HTML
        return HttpResponse(table_html)



class AdminSite(View):s
    def get(self, request):

        oj = Champion.objects.all()
        return render(request, 'admin.html', {"list":oj})