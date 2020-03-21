from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from news.models import Article
from news.forms import ArticleForm, Category
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
    carousels = Article.objects.filter(status=True,
                                       categories__exact='7'
                                       ).order_by('-timestamp')[:5]
    sliders = Article.objects.filter(status=True,
                                     categories__exact='9'
                                     ).order_by('-timestamp',)[:4]
    # national news
    national = Article.objects.filter(status=True, featured=True,
                                      categories__exact='9'
                                      ).order_by('-timestamp',)[:2]
    nationalcat = Article.objects.filter(status=True,
                                         categories__exact='9'
                                         ).order_by('-timestamp',
                                                    ).exclude(featured=True)

    context = {
        'carousels': carousels,
        'sliders': sliders,
        'national': national,
        'nationalcat': nationalcat,
        'title': 'Home'
    }
    return render(request, 'news/index.html', context)


# latest post Detail views
def Latest(request):
    obj = Article.objects.all().order_by('-timestamp',)

    context = {
        'object': obj,
        'title': 'تازہ ترین'
    }
    return render(request, 'news/latest.html', context)


# pakistan detail views
def pakistan(request):
    obj = Article.objects.filter(
        categories__exact='7').order_by('-timestamp',)

    context = {
        'object': obj,
        'title': 'پاکستان'
    }
    return render(request, 'news/pakistan.html', context)


# international detail viwes
def international(request):
    obj = Article.objects.filter(
        categories__exact='7').order_by('-timestamp',)

    context = {
        'object': obj,
        'title': 'بین الاقوامی خبریں'
    }
    return render(request, 'news/international.html', context)


# programes detail views
def programes(request):
    obj = Article.objects.filter(
        categories__exact='7').order_by('-timestamp',)

    context = {
        'object': obj,
        'title': ' پروگرامز'
    }
    return render(request, 'news/programes.html', context)


# showbiz detail views
def showbiz(request):
    obj = Article.objects.filter(
        categories__exact='7').order_by('-timestamp',)

    context = {
        'object': obj,
        'title': ' شوبز'
    }
    return render(request, 'news/showbiz.html', context)


# '''sports detial views'''
def sports(request):
    obj = Article.objects.filter(
        categories__exact='7').order_by('-timestamp',)

    context = {
        'object': obj,
        'title': ' سپورٹس'
    }
    return render(request, 'news/sports.html', context)


# live streeming views website
def Live(request):
    obj = Article.objects.filter(
        categories__exact='7').order_by('-timestamp',)

    context = {
        'object': obj,
        'title': 'live'
    }
    return render(request, 'news/live.html', context)


# live News Detail views website
def NewsDetail(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    context = {
        'object': obj
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
    # success_url = 'article-list'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk_)

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)


# DeleteViews


class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Article.objects.all()
    template_name = 'news/article_delete.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk_)

    def get_success_url(self):
        return reverse('article-list')
