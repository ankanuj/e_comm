from django.shortcuts import render,redirect
from products.models import *
from django.contrib import messages
from .models import *

def  cart(request):
    cart = Cart.objects.all().filter(user_id = request.user.id)
    price=Cart.objects.all().filter(user_id = request.user.id)
    address = Address.objects.all().filter(user_id = request.user.id)

    total_price = 0
    for price in price:
        total_price = total_price + price.products.price
    context = {
        'cart':cart,
        'total_price':total_price,
        'address':address,
    }
    if request.method == "POST":
        item = request.POST['item']
        remove = Cart.objects.get(pk=item)
        remove.delete()
        return render(request,'cart/cart.html',context)
    
    return render(request,'cart/cart.html',context)

def address(request):
    cart = Cart.objects.all()
   
    context = {
        'cart':cart,
        
    }

    if request.method == "POST":
        user_id = request.user.id
        address = request.POST['address']
        district = request.POST['district']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        mobile = request.POST['mobile']

        deliever = Address(user_id = user_id, address=address, state = state, district = district, zipcode=zipcode, mobile =mobile )
        deliever.save()
        return redirect('cart')


    return render(request,'cart/address.html')



def order(request):
    cart = Cart.objects.all()
   
    price=Cart.objects.all()
    address = Address.objects.all().filter(user_id = request.user.id)

    total_price = 0
    for price in price:
        total_price = total_price + price.products.price

    context = {
        'cart':cart,
        'total_price':total_price,
        'address':address,
            }

    if request.method == 'POST':
        address_id = request.POST['address']
        user_id = request.user.id
        product = request.POST['product']
        amount = total_price
        order_details = Order(user_id = user_id,address_id = address_id, amount = amount,product_id = product)
        order_details.save()
        messages.success(request,'Successfully ordered')
        
        return render(request,'cart/order.html',context)
        
  
    return render(request,'cart/order.html',context)
