from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    articles = Article.objects.order_by('-published_at').prefetch_related('scopes')
    return render(request, 'articles/news.html', {'object_list': articles})
