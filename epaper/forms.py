from taggit.models import Tag
from .models import Epaper
from django import forms


class EpaperForm(forms.ModelForm):

    class Meta:
        model = Epaper
        fields = ['title', 'image', 'tags', 'status', 'timestamp']
