from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)
    rate = models.FloatField()
    create_data = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} '

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=100, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

class Category(models.Model):
    img = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title
