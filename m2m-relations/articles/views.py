from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article, Scope


def articles_list(request):
    # articles = Article.objects.prefetch_related(Prefetch('scopes', queryset=Scope.objects.order_by(
    # 'title'))).order_by( '-published_at')
    articles = Article.objects.order_by('-published_at').prefetch_related('scopes')
    return render(request, 'articles/news.html', {'object_list': articles})
