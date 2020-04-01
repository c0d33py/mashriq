from django.shortcuts import render, get_object_or_404, reverse, redirect, get_list_or_404
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

    national = Article.status_objects.filter(
        tags__exact='1', featured=True)

    nationallist = Article.status_objects.filter(
        tags__exact='1').exclude(featured=True)[:4]

    # international
    worlds = Article.status_objects.filter(tags__exact='2', featured=True,)[:2]
    worldlists = Article.status_objects.filter(
        tags__exact='2').exclude(featured=True)[:4]
    # business
    Business = Article.status_objects.filter(tags__exact='2')[:4]
    #  sports
    sports = Article.status_objects.filter(tags__exact='4', featured=True)
    sportslist = Article.status_objects.filter(
        tags__exact='3').exclude(featured=True)[:4]
    # showbiz sidebar
    latest = Article.status_objects.all()[:5]
    footer = Article.status_objects.all()[:2]
    showbizs = Article.status_objects.filter(tags__exact='2')[:5]

    context = {
        'carousels': carousels,
        'sliders': sliders,
        'national': national,
        'nationallist': nationallist,
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
    obj = Article.objects.filter(status=True,).order_by('-timestamp',)
    latest = Article.objects.filter(status=True,
                                    categories__exact='12'
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      categories__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True,).order_by('-timestamp',)[:2]

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
    obj = Article.objects.filter(status=True,
                                 categories__exact='12').order_by('-timestamp',)
    latest = Article.objects.filter(status=True,
                                    categories__exact='12'
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      categories__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True,).order_by('-timestamp',)[:2]

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
    obj = Article.objects.filter(status=True,
                                 categories__exact='10').order_by('-timestamp',)
    latest = Article.objects.filter(status=True,
                                    categories__exact='12'
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      categories__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True,).order_by('-timestamp',)[:2]

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
    obj = Article.objects.filter(status=True,
                                 categories__exact='12').order_by('-timestamp',)
    latest = Article.objects.filter(status=True
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      categories__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True).order_by('-timestamp',)[:2]

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
    obj = Article.objects.filter(status=True,
                                 categories__exact='8').order_by('-timestamp',)
    latest = Article.objects.filter(status=True,
                                    categories__exact='12'
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      categories__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True).order_by('-timestamp',)[:2]

    context = {
        'object': obj,
        'showbizs': showbizs,
        'latest': latest,
        'footer': footer,
        'title': ' شوبز'
    }
    return render(request, 'news/showbiz.html', context)


# '''sports detial views'''
def sports(request):
    obj = Article.objects.filter(
        categories__exact='9').order_by('-timestamp',)
    latest = Article.objects.filter(status=True,
                                    categories__exact='12'
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      categories__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True,).order_by('-timestamp',)[:2]

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
    footer = Article.objects.all().order_by('-timestamp',)[:2]

    context = {
        'title': 'live'
    }
    return render(request, 'news/live.html', context)

# def trip_single(request, slug):
#     trip = get_object_or_404(Trip, slug=slug)
#     return render(request, 'app_trip/trip_single.html', {'trip': trip, 'trip_related': trip_related})


def NewsDetail(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    related = obj.tags.similar_objects()
    # print(related)

    # i want to  grab values like that

    # sidebar data
    latest = Article.objects.filter(status=True,
                                    ).order_by('-timestamp',)[:5]

    showbizs = Article.objects.filter(status=True,
                                      tags__exact='8'
                                      ).order_by('-timestamp',)[:5]
    footer = Article.objects.filter(status=True).order_by('-timestamp',)[:2]

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
    ordering = '-timestamp'
    template_name = 'news/article_list.html'

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
    # success_url = 'article-detail'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk_)

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.cleaned_data)
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
