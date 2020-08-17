from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'status', 'tag_list')
    # prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.unregister(Group)
admin.site.register(Article, ArticleAdmin)
