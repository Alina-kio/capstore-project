from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PopularBrand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Size(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.size

class Product(models.Model):
    title = models.CharField(max_length=30)
    brand = models.ForeignKey(PopularBrand, on_delete=models.CASCADE)
    original_price = models.IntegerField()
    discount_price = models.IntegerField(blank=True)
    size = models.ManyToManyField(Size)
    description = models.TextField(null=True)
    is_best_seller = models.BooleanField(default=False)
    is_favorite = models.BooleanField(blank=False)

    def __str__(self):
        return self.title



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title