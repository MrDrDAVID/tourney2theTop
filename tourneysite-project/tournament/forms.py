from dataclasses import fields
from django.forms import ModelForm
from .models import Tournament

class TournamentForm(ModelForm) :
    class Meta :
        model = Tournament
        fields = ['creator', 'game_title', 'description_rules', 'game_image', 
            'max_participants', 'winner']