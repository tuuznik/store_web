from django.db import models
from django.urls import reverse
from products.models import Product


class Item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"product_id": self.id}) #f"/products/{self.id}/"
