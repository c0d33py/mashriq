from django.contrib.sitemaps import Sitemap
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Article


class StaticViewSitemap(Sitemap):
    protocol = 'http'

    def items(self):
        return [
            'news-home',
            'news-latest',
            'news-pakistan',
            'news-international',
            'news-business',
            'news-showbiz',
            'news-sports',
        ]

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Article.status_objects.all()

    def lastmod(self, obj):
        return obj.timestamp
