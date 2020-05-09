from django.shortcuts import render
from products.models import *

def  cart(request,pk):
    if pk:
        product = Clothing.objects.all()
    if request.method =='POST':
        pass

    return render(request,'cart/cart.html')