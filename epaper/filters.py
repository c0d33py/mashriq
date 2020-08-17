import django_filters
from .models import Epaper


class EpaperFilter(django_filters.FilterSet):
    class Meta:
        model = Epaper
        fields = ['timestamp']
