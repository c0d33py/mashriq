from taggit.managers import TaggableManager
from django.shortcuts import reverse
from .thumbpath import article_path
from django.db import models
from PIL import Image


class EpaperQuerySet(models.Manager):
    def get_queryset(self):
        return super(EpaperQuerySet, self).get_queryset().filter(status=True)


class Epaper(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=article_path, verbose_name='Image')
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    status = models.BooleanField(default=True)
    objects = models.Manager()
    status_objects = EpaperQuerySet()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse('paper-detail', kwargs={'pk': self.pk})

    def get_success_url(self):
        return reverse('epaper-detail', kwargs={'pk': self.pk})
