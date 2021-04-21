from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(default='TBU')

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"article_id": self.id}) #f"/products/{self.id}/"

