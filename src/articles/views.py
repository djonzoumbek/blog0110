from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from articles.forms import ArticleForm, CategoryForm
from articles.models import Article


def home(request):
    return render(request, 'articles/home.html')


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "L'article a été ajouté avec succès !")
            return redirect("articles:home")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
            # Retourne la réponse avec le formulaire rempli avec les données invalides
            return render(request, 'articles/add_articles.html', {"form": form})
    else:
        form = ArticleForm()

    return render(request, 'articles/add_articles.html', {"form": form})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:home")
    else:
        form = CategoryForm()
        return render(request, 'articles/add_articles.html', {"form": form})


def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:home")

    else:
        form = ArticleForm(instance=article)
        return render(request, 'articles/add_articles.html', {"form": form})



def del_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("articles:list-articles")


def articles(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'articles/articles_list.html', context)


def show_article(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, 'articles/show_article.html', context)

# def like_article(request, pk):
#     article = Article.objects.get(pk=pk)
#     article.add_like()
#     return redirect('articles:show_article', article.pk)
