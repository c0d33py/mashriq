from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image
from datetime import datetime
import os


def set_filename_format(now, instance, filename):
    return "{date}-{microsecond}{extension}".format(
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def article_path(instance, filename):
    now = datetime.now()

    path = "article/{year}/{month}/{day}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        filename=set_filename_format(now, instance, filename),
    )
    return path


class ArticleQuerySet(models.Manager):
    def get_queryset(self):
        return super(ArticleQuerySet, self).get_queryset().filter(status=True).exclude(tags__exact='5')


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='def.jpg',
                                  upload_to=article_path)
    # same like models.URLField()
    video = EmbedVideoField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(blank=True)
    featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    tags = TaggableManager()
    objects = models.Manager()
    status_objects = ArticleQuerySet()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

    def save(self, *args, **kwargs):
        if self.featured == True:
            Article.objects.filter(pk__in=(Article.objects.filter(
                featured=True,).values_list('pk', flat=True)[:0])).update(featured=False)
            self.featured = True

        super(Article, self).save(*args, **kwargs)
        img = Image.open(self.thumbnail.path)
        if img.height > 400 or img.width > 700:
            output_size = (400, 700)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
