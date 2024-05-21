from django import forms
from .models import Tournament


class PostForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'

