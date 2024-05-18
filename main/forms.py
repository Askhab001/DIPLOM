from django import forms
from .models import LOL


class PostForm(forms.ModelForm):
    class Meta:
        model = LOL
        fields = '__all__'

