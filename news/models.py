from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    cat_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    categories = models.ManyToManyField(
        'Category', default='1--')
    thumbnail = models.ImageField(default='def.jpg',
                                  upload_to='article/thumbnails', blank=True, help_text='(optional)')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(blank=True)
    featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)

        img = Image.open(self.thumbnail.path)

        if img.height > 215 or img.width > 340:
            output_size = (215, 340)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
