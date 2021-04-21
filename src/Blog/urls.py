from django.urls import path
from .views import ArticleDeleteView, ArticleUpdateView, ArticleListView, ArticleDetailView, ArticleCreateView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:article_id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:article_id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:article_id>/delete/', ArticleDeleteView.as_view(), name='article-delete')]
