from django.forms import ModelForm
from django import forms
from .models import Champion, InfoMatch, Notification



class ChampionForm(forms.Form):
    team1_name = forms.CharField( max_length=30, required=True)
    team2_name = forms.CharField( max_length=30, required=True)
    score1 = forms.IntegerField()
    score2 = forms.IntegerField()
    
    
    
class InfoMatchForm(ModelForm):
    class Meta:
        model = InfoMatch
        fields = "__all__"
        
        
    
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"