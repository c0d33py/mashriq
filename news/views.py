from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from news.models import Article
from news.forms import ArticleForm
from .models import Article
from django.views.generic import (
    View,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


# index page of website
def index(request):
    carousels = Article.status_objects.filter(tags__exact='1')[:5]
    sliders = Article.status_objects.all().exclude(tags__exact='1')[:4]
    # national news
    featured_articles = Article.status_objects.filter(
        tags__exact='1', featured=True)[:2]

    regular_articles = Article.status_objects.filter(
        tags__exact='1').exclude(pk__in=featured_articles)[:7]

    # international
    worlds = Article.status_objects.filter(featured=True, tags__exact='2')[:2]
    worldlists = Article.status_objects.filter(
        tags__exact='2').exclude(featured=True)[:4]
    # videos
    videos = Article.objects.filter(status=True, tags__exact='5')[:4]
    #  columns
    featured_column = Article.status_objects.filter(
        featured=True, tags__exact='4')[:1]
    regular_column = Article.status_objects.filter(tags__exact='4'
                                                   ).exclude(featured=True)[:4]

    sports = Article.status_objects.filter(featured=True, tags__exact='3')[:1]
    sportslist = Article.status_objects.filter(tags__exact='3'
                                               ).exclude(featured=True)[:4]
    # showbiz sidebar
    latest = Article.status_objects.all().exclude(tags__exact='5')[:5]
    footer = Article.status_objects.all().exclude(tags__exact='5')[:2]
    showbizs = Article.status_objects.filter(
        tags__exact='4').exclude(tags__exact='5')[:5]

    context = {
        'carousels': carousels,
        'sliders': sliders,
        'national': featured_articles,
        'nationallist': regular_articles,
        'worlds': worlds,
        'worldlists': worldlists,
        'videos': videos,
        'featured_column': featured_column,
        'regular_column': regular_column,
        'sports': sports,
        'sportslist': sportslist,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': 'Home',
        'home': 'active',
    }
    return render(request, 'news/index.html', context)


# latest post Detail views
def Latest(request):
    obj = Article.status_objects.all()

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': 'تازہ ترین',
        'latests': 'active',

    }
    return render(request, 'news/latest.html', context)


# pakistan detail views
def pakistan(request):
    obj = Article.status_objects.filter(tags__exact='1')

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': 'پاکستان',
        'pakistan': 'active',

    }
    return render(request, 'news/pakistan.html', context)


# international detail viwes
def international(request):
    obj = Article.status_objects.filter(tags__exact='2')

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': 'بین الاقوامی خبریں',
        'international': 'active',

    }
    return render(request, 'news/international.html', context)


# programes detail views
def business(request):
    obj = Article.status_objects.filter(tags__exact='5')

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': ' کاروبار',
        'buisness': 'active',

    }
    return render(request, 'news/business.html', context)


# videos
def videos(request):
    obj = Article.objects.filter(status=True, tags__exact='5')

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': ' ویڈیوز',
        'videos': 'active',

    }
    return render(request, 'news/videos.html', context)


# showbiz detail views
def showbiz(request):
    obj = Article.status_objects.filter(tags__exact='4')

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='3')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': ' شوبز',
        'title2': ' سپورٹس',
        'showbiz': 'active',

    }
    return render(request, 'news/showbiz.html', context)


# '''sports detial views'''
def sports(request):
    obj = Article.status_objects.filter(tags__exact='3')

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': ' سپورٹس',
        'sports': 'active',

    }
    return render(request, 'news/sports.html', context)


# live streeming views website
def Live(request):
    footer = Article.status_objects.all()[:2]

    context = {
        'title': 'live'
    }
    return render(request, 'news/live.html', context)


# live News Detail views website
def NewsDetail(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    related = obj.tags.similar_objects()[:3]

    latest = Article.status_objects.all()[:5]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]
    footer = Article.status_objects.all()[:2]

    context = {
        'object': obj,
        'related': related,
        'showbizs': showbizs,
        'footer': footer,
        'latest': latest
    }
    return render(request, 'news/detail.html', context)


# videos detail page
def VideoDetail(request, pk):
    videos = get_object_or_404(Article, tags__exact='5', pk=pk)
    related = videos.tags.similar_objects()[:3]

    context = {
        'videos': videos,
        'related': related,
    }
    return render(request, 'news/detail.html', context)


# admin side views
# this view is class base and user authenticated
# CreateViews

class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    template_name = 'news/article_create.html'
    success_url = '/article/list/'
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


# ListViews


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    queryset = Article.objects.all()
    context_object_name = 'articles'
    template_name = 'news/article_list.html'


# draft post list view
class ArticleDraftListView(LoginRequiredMixin, ListView):
    model = Article
    queryset = Article.objects.filter(status=False)
    context_object_name = 'articles'
    template_name = 'news/draft_post_list.html'

# DetailViews


class ArticleDetailView(LoginRequiredMixin, DetailView):
    queryset = Article.objects.all()
    template_name = 'news/article_detail.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk_)

# UpdateViews


class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ArticleForm
    template_name = 'news/article_create.html'
    success_message = "%(title)s was created successfully"
    # success_url = 'article-list'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk_)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


# DeleteViews


class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Article.objects.all()
    template_name = 'news/article_delete.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk_)

    def get_success_url(self):
        return reverse('article-list')
