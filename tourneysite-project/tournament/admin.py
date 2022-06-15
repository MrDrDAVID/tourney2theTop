from django.contrib import admin
from .models import Tournament, Participants, Matches

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Participants)
admin.site.register(Matches)