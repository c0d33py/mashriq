from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, NewsSitemap
from django.urls import path
from . import views
from .views import (ArticleListView,
                    ArticleDraftListView,
                    ArticleCreateView,
                    ArticleDetailView,
                    ArticleUpdateView,
                    ArticleDeleteView
                    )
sitemaps = {
    'static': StaticViewSitemap,
    'news': NewsSitemap,
}


urlpatterns = [
    # client side interface
    path('', views.index, name='news-home'),
    path('latest/', views.Latest, name='news-latest'),
    path('pakistan/', views.pakistan, name='news-pakistan'),
    path('international/', views.international, name='news-international'),
    path('business/', views.business, name='news-business'),
    path('showbiz/', views.showbiz, name='news-showbiz'),
    path('sports/', views.sports, name='news-sports'),
    path('videos/', views.videos, name='news-videos'),
    path('news/detail/<int:pk>/', views.NewsDetail, name='news-detail'),
    path('video/detail/<int:pk>/', views.VideoDetail, name='video-detail'),
    path('news/live/', views.Live, name='news-streem'),
    # sitemap
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),


    # this urls for user interface
    path('article/list/', ArticleListView.as_view(), name='article-list'),
    path('article/draft/', ArticleDraftListView.as_view(), name='article-draft'),
    path('article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/detail/',
         ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/update/',
         ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article-delete'),
]
