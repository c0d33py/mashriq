from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Prompter(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    content = RichTextField()

    def get_absolute_url(self):
        return reverse('promp-detail', kwargs={'pk': self.pk})

    def get_success_url(self):
        return reverse('promp-update', kwargs={'pk': self.pk})
