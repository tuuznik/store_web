from django.shortcuts import get_object_or_404, render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, ListView, DeleteView
from django.urls import reverse


class ArticleListView(ListView):
    template_name = "articles/articles_list.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('article_id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('article_id')
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('article_id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:articles-list')
