from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField
from django.shortcuts import reverse, redirect
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from .manager import ArticleQuerySet
from .imagename import article_path
from unidecode import unidecode
from django.db import models
from PIL import Image


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='def.jpg', upload_to=article_path)
    video = EmbedVideoField(blank=True, null=True)  # past video URL
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
        '''post filter'''
        if self.featured == True:
            Article.objects.filter(pk__in=(Article.objects.filter(
                featured=True,).values_list('pk', flat=True)[:0])).update(featured=False)
            self.featured = True

        '''image size reduce'''
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
