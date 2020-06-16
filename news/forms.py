from django.forms.widgets import CheckboxSelectMultiple
from django import forms
from taggit.models import Tag
from . models import Article


class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Article
        fields = ['title', 'thumbnail', 'tags',
                  'content', 'video', 'featured', 'status']
