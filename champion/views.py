from django.shortcuts import render
from django.views import View
from .models import Champion
from django.http import HttpResponse
# Create your views here.



def sort_key(champion):
    return (-champion.point, -champion.h_s)

def ranking_view(request):
    # Lấy tất cả các đối tượng từ database và sắp xếp
    teams_from_db = Champion.objects.all().order_by('-point', '-h_s')
    
    # Đặt rank cho các đội dựa trên thứ tự sắp xếp
    rank = 1
    for team in teams_from_db:
        team.rank = rank
        rank += 1
    
    # Tạo nội dung HTML từ danh sách đã sắp xếp và đã thêm rank
    table_html = "<table>"
    for team in teams_from_db:
        table_html += f"<tr><td>{team.rank}</td><td>{team.name}</td><td>{team.point}</td><td>{team.h_s}</td></tr>"
    table_html += "</table>"
    
    # Trả về HttpResponse chứa nội dung HTML
    response = HttpResponse(table_html)
    return response


class Main(View):
    def get(self, request):

        # xét xếp hạng dựa trên điểm, và điểm bằng nhau xét tới HS
        list_object = Champion.objects.all()
        def sort_key(team):
            return (-team.point, -team.h_s)

         # Sắp xếp danh sách các đối tượng
        sorted_teams = sorted(list_object, key=sort_key)

# In danh sách đã sắp xếp
        for team in sorted_teams:
            print(f"Name: {team.name}, Point: {team.point}, H/S: {team.h_s}")

        return render(request, 'main.html')
    



class AdminSite(View):
    def get(self, request):

        oj = Champion.objects.all()
        return render(request, 'admin.html', {"list":oj})