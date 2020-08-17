from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    path('', include('news.urls')),
    path('epaper/', include('epaper.urls')),
    path('admin/', views.Dashboard, name='dashboard'),
    path('django/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('robots.txt/', include('robots.urls')),
    path('ads.txt', include('ads_txt.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
