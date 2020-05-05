from django.shortcuts import render
from .models import *

def products(request):
    if 'product/mens/shirts' in request.path:
        products = Clothing.objects.all().filter(product_type='shirt',gender='M',category='Mens')
    elif 'product/mens/t-shirts' in request.path:
        products = Clothing.objects.all().filter(product_type='t-shirt',gender='M',category='Mens')
    elif 'product/mens/jeans' in request.path:
        products = Clothing.objects.all().filter(product_type='jeans',gender='M',category='Mens')
    elif 'product/mens/trousers' in request.path:
        products = Clothing.objects.all().filter(product_type='trousers',gender='M',category='Mens')
    
    #Womens section
    elif 'product/womens/shirts' in request.path:
        products = Clothing.objects.all().filter(product_type='shirt',gender='F',category='womens')
    elif 'product/womens/t-shirts' in request.path:
        products = Clothing.objects.all().filter(product_type='t-shirt',gender='F',category='womens')
    elif 'product/womens/jeans' in request.path:
        products = Clothing.objects.all().filter(product_type='jenas',gender='F',category='womens')
    elif 'product/womens/trousers' in request.path:
        products = Clothing.objects.all().filter(product_type='trousers',gender='F',category='womens')
    
    #kids section
    elif 'product/kids/shirts' in request.path:
        products = Clothing.objects.all().filter(product_type='shirt',category='kids')
    elif 'product/kids/t-shirts' in request.path:
        products = Clothing.objects.all().filter(product_type='t-shirt',category='kids')
    elif 'product/kids/jeans' in request.path:
        products = Clothing.objects.all().filter(product_type='jenas',category='kids')
    elif 'product/kids/trousers' in request.path:
        products = Clothing.objects.all().filter(product_type='trousers',category='kids')
    
    context = {
        'products':products,
    }
    return render(request,'shop/products.html',context)

def product_details(request,pk):
    product = Clothing.objects.get(pk=pk)
    context={
        'product':product,
    } 

    return render(request,'products_details/product_details.html',context)
