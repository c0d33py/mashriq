from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from news.models import Article


@login_required
def Dashboard(request):
    articles = Article.objects.all()
    context = {
        'title': 'Dashboard',
        'articles': articles
    }
    return render(request, 'dashboard.html', context)
