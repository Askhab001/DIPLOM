from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    personal_data = models.TextField()
    contact_info = models.CharField(max_length=100)


class Schedule(models.Model):
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    # Other fields for match details


class Result(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    # Other fields for match result details
