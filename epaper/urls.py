# from .sitemaps import StaticViewSitemap, NewsSitemap
from django.contrib.sitemaps.views import sitemap
from news.sitemaps import StaticViewSitemap, NewsSitemap
from django.urls import path
from . import views
from .views import (
    EpaperListView,
    EpaperDraftListView,
    EpaperDetailView,
    EpaperCreateView,
    EpaperUpdateView,
    EpaperDeleteView,
    # EpaperCreate
)
sitemaps = {
    'static': StaticViewSitemap,
    'epaper': NewsSitemap,
}


urlpatterns = [
    path('', views.index, name='paper-home'),
    path('detail/<int:pk>/', views.EpaperDetail, name='paper-detail'),

    # sitemap
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),


    # this urls for user interface
    path('list/', EpaperListView.as_view(), name='epaper-list'),
    path('draft/', EpaperDraftListView.as_view(), name='epaper-draft'),
    path('create/', EpaperCreateView.as_view(), name='epaper-create'),
    path('epaper/detail/<int:pk>/',
         EpaperDetailView.as_view(), name='epaper-detail'),
    path('update/<int:pk>/',
         EpaperUpdateView.as_view(), name='epaper-update'),
    path('delete/<int:pk>/',
         EpaperDeleteView.as_view(), name='epaper-delete'),
]
