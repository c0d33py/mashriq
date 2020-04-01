from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from .models import Article


class LatestArticleFeed(Feed):
    title = 'some tile'

    def items(self):
        return Article.status_objects.all()

    def item_title(self, item):
        return item.title
