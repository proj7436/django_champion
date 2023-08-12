from django.db import models

# Create your models here.

class Champion(models.Model):
    rank = models.IntegerField()
    name_team = models.CharField(max_length=30)
    count_round = models.IntegerField()
    count_win =models.IntegerField()
    count_lose = models.IntegerField()
    count_draw = models.IntegerField()
    goal = models.IntegerField()
    goal_conceded = models.IntegerField()
    h_s = models.IntegerField()
    point = models.IntegerField()
    def __str__(self) -> str:
        return self.name_team




class InfoMatch(models.Model):
    info = models.CharField(max_length=255)
    time = models.CharField(max_length=25)
    
    
    
class Notification(models.Model):
    noti = models.CharField(max_length = 255, default='Vui là 9, Thắng là 10.')