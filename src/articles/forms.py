from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'category',
            'tags',
            'author',
            'image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
            'description': SummernoteWidget(attrs={'class': 'form-control'}),
            # Utilisation de Summernote pour la description
            'category': forms.SelectMultiple(attrs={'class': 'form-select'}),
            # Champ pour sélectionner plusieurs catégories
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags'}),
            'author': forms.Select(attrs={'class': 'form-select'}),  # Sélection d’auteur
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Upload de fichier avec Bootstrap
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
