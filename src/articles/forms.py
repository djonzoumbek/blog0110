from django import forms
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
        """widgets = {
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
        }"""


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'