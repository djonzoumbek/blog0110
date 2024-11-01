from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Category


# Configurer l’éditeur Summernote pour les champs spécifiques
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'author',
        'published_date',
        'published',
        'nb_likes',
        'nb_dislikes',
    ]
    list_editable = ('published_date',)
    # Appliquer Summernote seulement au champ 'description'
    summernote_fields = ('description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]
