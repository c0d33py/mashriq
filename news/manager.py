from django.db import models


class ArticleQuerySet(models.Manager):
    def get_queryset(self):
        return super(ArticleQuerySet, self).get_queryset().filter(status=True).exclude(tags__exact='5')
