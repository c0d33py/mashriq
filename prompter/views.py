from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Prompter
from .forms import PrompForm


def Blank(request):
    return render(request, 'prompter/blank.html')


def ScreenView(request, pk):
    obj = get_object_or_404(Prompter, pk=pk)
    context = {
        'object': obj
    }
    return render(request, 'prompter/screen_view.html', context)


# CreateViews

class PrompterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PrompForm
    template_name = 'prompter/prompter_create.html'
    success_url = '/prompter/list/'
    success_message = "created successfully"

    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


class PrompterListView(LoginRequiredMixin, ListView):
    model = Prompter
    queryset = Prompter.objects.all()
    context_object_name = 'prompters'
    template_name = 'prompter/prompter_list.html'


# draft post list view
class PrompterDraftListView(LoginRequiredMixin, ListView):
    model = Prompter
    queryset = Prompter.objects.filter(status=False)
    context_object_name = 'prompters'
    template_name = 'prompter/draft_prompter_list.html'

# DetailViews


class PrompterDetailView(LoginRequiredMixin, DetailView):
    queryset = Prompter.objects.all()
    template_name = 'prompter/prompter_detail.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Prompter, pk=pk_)

# UpdateViews


class PrompterUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = PrompForm
    template_name = 'prompter/prompter_create.html'
    success_message = "created successfully"

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Prompter, pk=pk_)

    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return self.object.get_success_url()


# DeleteViews


class PrompterDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Prompter.objects.all()
    template_name = 'prompter/prompter_delete.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Prompter, pk=pk_)

    def get_success_url(self):
        return reverse('promp-list')
