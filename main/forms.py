# tournaments/forms.py
from django import forms
from .models import Tournament, Participant, Schedule, Result


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['title', 'description', 'date', 'location']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['personal_data', 'contact_info']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['match_date', 'details']


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['details']
