from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Article


admin.site.register(Article)
