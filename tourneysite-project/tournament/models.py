from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tournament(models.Model) :
    class MaxParticipants(models.IntegerChoices) :
        SMALL = 16
        MEDIUM = 32
        LARGE = 64
        X_LARGE = 128

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    game_title = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    description_rules = models.TextField()
    game_image = models.ImageField(blank=True)
    max_participants = models.IntegerField(choices=MaxParticipants.choices)
    winner = models.CharField(max_length=30, blank=True)

    def __str__(self) :
        return self.game_title

    class Meta :
        ordering = ['-date_posted']

class Participants(models.Model) :
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.participant.username

    class Meta :
        verbose_name_plural = 'Participants'

class Matches(models.Model) :
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    competitor_one = models.ForeignKey(User, related_name='competitor_one', on_delete=models.CASCADE)
    competitor_two = models.ForeignKey(User, related_name='competitor_two', on_delete=models.CASCADE)
    round_num = models.IntegerField()
    winner = models.CharField(max_length=30, blank=True)
    loser = models.CharField(max_length=30, blank=True)

    def __str__(self) :
        return self.competitor_one.username + ' vs ' + self.competitor_two.username

    class Meta :
        verbose_name_plural = 'Matches'