from django.contrib.sitemaps import Sitemap
from itertools import chain
from django.urls import reverse
from .models import Article
from epaper.models import Epaper


class StaticViewSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return [
            'news-home',
            'news-latest',
            'news-pakistan',
            'news-international',
            'news-business',
            'news-showbiz',
            'news-sports',
            'paper-home',
        ]

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        sitePaper = Epaper.status_objects.all()
        siteNews = Article.status_objects.all()
        site_list = list(
            chain(sitePaper, siteNews)
        )
        return site_list

    def lastmod(self, obj):
        return obj.timestamp
