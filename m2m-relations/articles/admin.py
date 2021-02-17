from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleScope, Scope

MSG_MAIN_SCOPE_DELETE_NOT_ALLOWED = 'Ошибка! Нельзя удалять главную рубрику.'
MSG_TWO_MAIN_SCOPES_NOT_ALLOWED = 'Ошибка! Выбрано более двух главных рубрик.'
MSG_MAIN_SCOPE_IS_EMPTY_NOT_ALLOWED = 'Ошибка! Не задана главная рубрика.'


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_present = False
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main', False)
            delete = form.cleaned_data.get('DELETE', False)
            if delete and is_main:
                raise ValidationError(MSG_MAIN_SCOPE_DELETE_NOT_ALLOWED)
            if is_main_present and is_main:
                raise ValidationError(MSG_TWO_MAIN_SCOPES_NOT_ALLOWED)
            elif is_main:
                is_main_present = True
        if not is_main_present:
            raise ValidationError(MSG_MAIN_SCOPE_IS_EMPTY_NOT_ALLOWED)
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleScopeInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    model = Scope
