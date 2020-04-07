from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from news.models import Article
from news.forms import ArticleForm
from .models import Article
from django.views.generic import (
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
    worlds = Article.status_objects.filter(featured=True, tags__exact='2')[:1]
    worldlists = Article.status_objects.filter(
        tags__exact='2').exclude(featured=True)[:4]
    # business
    Business = Article.status_objects.filter(tags__exact='5')[:4]
    #  sports
    sports = Article.status_objects.filter(featured=True, tags__exact='3')[:1]
    sportslist = Article.status_objects.filter(tags__exact='3'
                                               ).exclude(featured=True)[:4]
    # showbiz sidebar
    latest = Article.status_objects.all()[:5]
    footer = Article.status_objects.all()[:2]
    showbizs = Article.status_objects.filter(tags__exact='4')[:5]

    context = {
        'carousels': carousels,
        'sliders': sliders,
        'national': featured_articles,
        'nationallist': regular_articles,
        'worlds': worlds,
        'worldlists': worldlists,
        'business': Business,
        'sports': sports,
        'sportslist': sportslist,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': 'Home'
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
        'title': 'تازہ ترین'
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
        'title': 'پاکستان'
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
        'title': 'بین الاقوامی خبریں'
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
        'title': ' کاروبار'
    }
    return render(request, 'news/business.html', context)


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
        'title2': ' سپورٹس'
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
        'title': ' سپورٹس'
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
        print(form.cleaned_data)
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
