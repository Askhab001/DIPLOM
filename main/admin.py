# tournaments/admin.py
from django.contrib import admin
from .models import Tournament, Participant, Schedule, Result

admin.site.register(Tournament)
admin.site.register(Participant)
admin.site.register(Schedule)
admin.site.register(Result)
