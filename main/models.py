# tournaments/models.py
from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    personal_data = models.TextField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.tournament.title}'


class Schedule(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    details = models.TextField()

    def __str__(self):
        return f'{self.tournament.title} - {self.match_date}'


class Result(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return f'{self.tournament.title} - {self.details}'
