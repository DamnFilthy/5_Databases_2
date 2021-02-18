from django.db.models import Prefetch
from django.shortcuts import render
from articles.models import Article, ArticleScope


def articles_list(request):
    # Оптимизированная выборка сортированная по двум полям
    articles = Article.objects.order_by('-published_at').prefetch_related(Prefetch(
            'scopes',
            queryset=ArticleScope.objects.select_related(
                'topic'
            ).order_by('-is_main', 'topic'),
        ),
    )
    # Оптимизированная выборка
    # articles = Article.objects.order_by('-published_at').prefetch_related(
    #     Prefetch('scopes', queryset=ArticleScope.objects.order_by('topic').select_related('topic')))

    # Обычная выборка
    # articles = Article.objects.order_by('-published_at').prefetch_related('scopes')
    return render(request, 'articles/news.html', {'object_list': articles})
