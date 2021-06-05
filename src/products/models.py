from django.db import models
from django.urls import reverse
from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True, default=None)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"product_id": self.id}) #f"/products/{self.id}/"
