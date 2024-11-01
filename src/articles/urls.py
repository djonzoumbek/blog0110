from django.urls import path
from .views import home, add_article, add_category, edit_article, del_article, articles, show_article

app_name = 'articles'
urlpatterns = [
    path('', home, name='home' ),
    path('list-articles', articles, name='list-articles' ),
    path('add-article/', add_article, name='add_article' ),
    path('add-category/', add_category, name='add_category' ),
    path('edit-article/<int:pk>/', edit_article, name='edit_article' ),
    path('del-article/<int:pk>/', del_article, name='del_article' ),
    path('show-article/<int:pk>/', show_article, name='show_article' ),
    #path('like-article/<int:pk>/like', like_article, name='like_article' ),

]