from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tournament(models.Model) :
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    game_title = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    description_rules = models.TextField()
    game_image = models.ImageField()

    def __str__(self) :
        return self.game_title

    class Meta :
        ordering = ['-date_posted']

class Participants(models.Model) :
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.participant.username

class Matches(models.Model) :
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    competitor_one = models.ForeignKey(User, related_query_name='competitor_one')
    competitor_two = models.ForeignKey(User, related_name='competitor_two')
    round_num = models.IntegerField()