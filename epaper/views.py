from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from news.models import Article
from .forms import EpaperForm
from .models import Epaper
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


# index page of website
def index(request):
    images = Epaper.status_objects.all()

    footer = Article.status_objects.all().exclude(tags__exact='5')[:2]

    context = {
        'images': images,
        'footer': footer,
        'title': 'Epaper',
        'paperHome': 'active',
    }
    return render(request, 'paper/index.html', context)

# live News Detail views website


def EpaperDetail(request, pk):
    obj = get_object_or_404(Epaper, pk=pk)
    relat = obj.tags.similar_objects()

    footer = Article.status_objects.all().exclude(tags__exact='5')[:2]
    context = {
        'object': obj,
        'relat': relat,
        'footer': footer,
        'paper': 'paper',
    }
    return render(request, 'paper/detail.html', context)

# admin side views
# this view is class base and user authenticated
# CreateViews


class EpaperCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = EpaperForm
    template_name = 'paper/epaper_create.html'
    success_message = "%(title)s was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


# # ListViews


class EpaperListView(LoginRequiredMixin, ListView):
    model = Epaper
    context_object_name = 'epapers'
    template_name = 'paper/epaper_list.html'


# draft post list view
class EpaperDraftListView(LoginRequiredMixin, ListView):
    # model = Article
    queryset = Epaper.objects.filter(status=False)
    context_object_name = 'epapers'
    template_name = 'paper/draft_post_list.html'

# # DetailViews


class EpaperDetailView(LoginRequiredMixin, DetailView):
    model = Epaper
    template_name = 'paper/epaper_detail.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Epaper, pk=pk_)

# # UpdateViews


class EpaperUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = EpaperForm
    template_name = 'paper/epaper_create.html'
    success_message = "%(title)s was created successfully"

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Epaper, pk=pk_)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


# # DeleteViews


class EpaperDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Epaper
    template_name = 'paper/epaper_delete.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Epaper, pk=pk_)

    def get_success_url(self):
        return reverse('epaper-list')
