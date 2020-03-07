from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from . models import Article
from . models import Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'categories', 'thumbnail', 'content']
        widgets = {
            'categories': CheckboxSelectMultiple(),
        }


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
