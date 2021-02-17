from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    articles = models.ManyToManyField(Article, through='ArticleScope')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    topic = models.ForeignKey(Scope, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Главный тэг')

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.topic)
