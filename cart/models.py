from django.db import models
from django.conf import settings
from mamazon.models import Product

User = setting.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2) 1,000,000.00
    created = models.models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




# Create your models here.
