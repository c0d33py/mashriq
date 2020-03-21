from django.urls import path
from . import views
from .views import (ArticleListView,
                    ArticleCreateView,
                    ArticleDetailView,
                    ArticleUpdateView,
                    ArticleDeleteView
                    )


urlpatterns = [
    # client side interface
    path('', views.index, name='news-home'),
    path('latest/', views.Latest, name='news-latest'),
    path('pakistan/', views.pakistan, name='news-pakistan'),
    path('international/', views.international, name='news-international'),
    path('programes/', views.programes, name='news-programes'),
    path('showbiz/', views.showbiz, name='news-showbiz'),
    path('sports/', views.sports, name='news-sports'),
    path('news/<int:pk>/detail/', views.NewsDetail, name='news-detail'),
    path('news/live/', views.Live, name='news-streem'),


    # this urls for user interface
    path('article/list/', ArticleListView.as_view(), name='article-list'),
    path('article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/detail/',
         ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/update/',
         ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article-delete'),
]
