from django.shortcuts import render
from django.views import View
from .models import Champion, Notification, InfoMatch
from django.http import HttpResponse
from .forms import ChampionForm, NotificationForm, InfoMatchForm
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
        
        oj_noti = Notification.objects.get(id=1)
        oj_info_match = InfoMatch.objects.all()
        # Trả về HttpResponse chứa nội dung HTML
        return render(request, 'main.html', {'sorted_champions': sorted_champions, 'noti':oj_noti.noti, 'list_info_match':oj_info_match})


class AdminSite(View):
    def get(self, request):

        oj = Champion.objects.all()
        return render(request, 'admin.html', {"list":oj})
    

    def post(self, request):

        oj = Champion.objects.all()
        
        input_ = request.POST
        form = ChampionForm(request.POST)

        if form.is_valid():
            team1_name = input_.get('team1_name')
            team2_name = input_.get('team2_name')
            
            score1 = int(input_.get('score1'))
            score2 = int(input_.get('score2'))

            oj1 = Champion.objects.get(id = team1_name)
            oj2 = Champion.objects.get(id = team2_name)

            if score1 > score2:
                oj1.count_win += 1
                oj1.point += 3
                
                oj1.goal += score1
                oj2.goal += score2
                
                oj1.goal_conceded += score2
                oj2.goal_conceded += score1
                
                oj2.count_lose += 1
            elif score1== score2:
                oj1.count_draw += 1
                oj2.count_draw += 1
                
                oj1.goal += score1
                oj2.goal += score2
                
                oj1.goal_conceded += score2
                oj2.goal_conceded += score1
                
                oj1.point += 1
                oj2.point += 1
            else:
                oj1.count_lose += 1
                oj2.count_win += 1
                oj2.point += 3
                
                oj1.goal += score1
                oj2.goal += score2
                
                oj1.goal_conceded += score2
                oj2.goal_conceded += score1
            
            #cộng điểm số trận 
            oj1.count_round += 1
            oj2.count_round += 1
            
            oj1.h_s = oj1.goal - oj1.goal_conceded
            oj2.h_s = oj2.goal - oj2.goal_conceded
            
            oj1.save()
            oj2.save()

            return render(request, 'admin.html', context={'message':'Cap nhat thanh cong!', 'list':oj})
        return render(request, 'admin.html', context={'message':'error', 'list':oj})
    
    
    
    

class HandleNoti(View):
    def post(self, request):
        oj = Champion.objects.all()
        data = request.POST
        form = NotificationForm(data)
        
        if form.is_valid():
            noti_ = data.get('noti')
            
            oj_ = Notification.objects.get(id=1)
            oj_.noti = noti_
            
            oj_.save()
            return render(request, 'admin.html', context={'message1':'Cap nhat thanh cong!', 'list':oj})
        return render(request, 'admin.html', context={'message1':'error', 'list':oj})
    
    
    
class HandleInfoMatch(View):
    def post(self, request):
        oj = Champion.objects.all()
        data = request.POST
        form = InfoMatchForm(data)
        
        if form.is_valid():
            time = data.get('time')
            info = data.get('info')
            
            InfoMatch.objects.create(time = time, info = info)    
            return render(request, 'admin.html', context={'message2':'Cap nhat thanh cong!', 'list':oj})
        return render(request, 'admin.html', context={'message2':'error', 'list':oj})
    
    
    
    
    


