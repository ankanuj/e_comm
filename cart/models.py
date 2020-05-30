from django.db import models
from products.models import *
from django.contrib.auth.models import User
from datetime import datetime


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username

class Delivery_Address(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now, null=True)
    address = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.user.username