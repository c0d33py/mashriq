from django import forms
from .models import Prompter


class PrompForm(forms.ModelForm):
    class Meta:
        model = Prompter
        fields = ['content', 'status']
