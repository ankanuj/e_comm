from django.db import models
from products.models import *


class Cart(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

