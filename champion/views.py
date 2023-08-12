from django.shortcuts import render
from django.views import View
from .models import Champion
from django.http import HttpResponse
from .forms import ChampionForm
# Create your views here.




class Main(View):
    def get(self, request):
        # Lấy danh sách các đối tượng từ database
        champions = Champion.objects.all()
        
        # Sắp xếp danh sách đối tượng theo điểm số tăng dần, sau đó theo hiệu số giảm dần
        sorted_champions = sorted(champions, key=lambda x: (x.point, x.h_s), reverse=True)
        
        # Thêm một thuộc tính mới "index" cho mỗi đối tượng champion
        for index, champion in enumerate(sorted_champions, start=1):
            champion.index = index
        
        # Trả về HttpResponse chứa nội dung HTML
        return render(request, 'main.html', {'sorted_champions': sorted_champions})


class AdminSite(View):
    def get(self, request):

        oj = Champion.objects.all()
        return render(request, 'admin.html', {"list":oj})
    

    def post(self, request):

        input_ = request.POST
        form = ChampionForm(request.POST)

        if form.is_valid():
            team1_name = input_.get('team1_name')
            team2_name = input_.get('team2_name')

            score1 = input_.get('score1')
            score2 = input_.get('score2')

            oj1 = Champion.objects.get(name_team = team1_name)
            oj2 = Champion.objects.get(name_team = team2_name)

            if score1 > score2:
                oj1.count_win += 1
                oj2.count_lose += 1
            elif score1== score2:
                oj1.count_draw += 1
                oj2.count_draw += 1
            else:
                oj1.count_lose += 1
                oj2.count_win += 1

            oj1.save()
            oj2.save()

            return render(request, 'admin.html', context={'message':'Cap nhat thanh cong!'})
        return render(request, 'admin.html', context={'message':'error'})