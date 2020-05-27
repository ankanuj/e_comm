from django.shortcuts import render
from products.models import *
from .models import *

def  cart(request):
    cart = Cart.objects.all()
    price=Cart.objects.all()

    total_price = 0
    for price in price:
        total_price = total_price + price.products.price
    context = {
        'cart':cart,
        'total_price':total_price,
    }
    if request.method == "POST":
        item = request.POST['item']
        remove = Cart.objects.get(pk=item)
        remove.delete()
        return render(request,'cart/cart.html',context)
    
    return render(request,'cart/cart.html',context)
