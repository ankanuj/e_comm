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

class Address(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now, null=True)
    address = models.TextField(max_length=1000, null=False)
    state = models.CharField(max_length=50,null=False)
    district = models.CharField(max_length=50,null=False)
    zipcode = models.IntegerField()
    mobile = models.IntegerField()
    

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    placed_on = models.DateTimeField(default= datetime.now)
    product = models.ForeignKey(Cart, on_delete = models.CASCADE)
    address = models.ForeignKey(Address,on_delete = models.CASCADE)
    amount = models.FloatField(default=0)

    def __str__(self):
        return  self.user.username


class PaymentDetails(models.Model):
    trsn_date = models.CharField(verbose_name="Transaction Date",max_length=100)
    trsn_id = models.CharField(verbose_name="Transaction id",max_length=100)
    order_id = models.CharField(verbose_name="Order Id",max_length=100)
    trsn_amount = models.CharField(verbose_name="Transaction Amount",max_length=100)
    trsn_status = models.CharField(max_length=100)

    def __str__(self):
        return  self.order_id