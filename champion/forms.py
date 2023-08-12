from django.forms import ModelForm
from .models import Champion



class ChampionForm(ModelForm):
    class Meta:
        model = Champion
        fields = ('point', 'name_team')