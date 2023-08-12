from django.shortcuts import render
from django.views import View
from .models import Champion
from django.http import HttpResponse
# Create your views here.




class Main(View):
    def get(self, request):
        # Lấy danh sách các đối tượng từ database
        champions = Champion.objects.all()
        
        # Sắp xếp danh sách đối tượng theo điểm số tăng dần, sau đó theo hiệu số giảm dần
        sorted_champions = sorted(champions, key=lambda x: (x.point, -x.h_s), reverse=True)
        
        # Tạo nội dung HTML từ danh sách đã sắp xếp
        table_html = "<table>"
        for index, champion in enumerate(sorted_champions, start=1):
            table_html += f"<tr><td>{index}</td><td>{champion.name}</td><td>{champion.point}</td><td>{champion.h_s}</td></tr>"
        table_html += "</table>"
        
        # Trả về HttpResponse chứa nội dung HTML
        return HttpResponse(table_html)


class AdminSite(View):
    def get(self, request):

        oj = Champion.objects.all()
        return render(request, 'admin.html', {"list":oj})