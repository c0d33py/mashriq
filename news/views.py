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
    carousels = Article.objects.filter().order_by('-timestamp')[:5]
    sliders = Article.objects.filter(
        categories__isnull='1').order_by('-timestamp',)[:4]

    context = {
        'carousels': carousels,
        'sliders': sliders,
    }
    return render(request, 'news/index.html', context)


def NewsDetail(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    context = {
        'obj': obj
    }
    return render(request, 'news/detail.html', context)


# live streeming views website
def Live(request):
    return render(request, 'news/live.html')


# admin side views
# this view is class base and user authenticated
# CreateViews

class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    template_name = 'news/article_create.html'
    success_url = '/article/list/'
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
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
