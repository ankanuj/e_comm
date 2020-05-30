from django.shortcuts import render
from .models import *
from cart.models import Cart

#Clothing products view function
def products(request):
    if 'product/mens/clothing/shirts' in request.path:
        products = Products.objects.all().filter(product_type='shirt',gender='M',category='Mens')
    elif 'product/mens/clothing/t-shirts' in request.path:
        products = Products.objects.all().filter(product_type='t-shirt',gender='M',category='Mens')
    elif 'product/mens/clothing/jeans' in request.path:
        products = Products.objects.all().filter(product_type='jeans',gender='M',category='Mens')
    elif 'product/mens/clothing/trousers' in request.path:
        products = Products.objects.all().filter(product_type='trousers',gender='M',category='Mens')
    
    #Womens section
    elif 'product/womens/clothing/shirts' in request.path:
        products = Products.objects.all().filter(product_type='shirt',gender='F',category='womens')
    elif 'product/womens/clothing/t-shirts' in request.path:
        products = Products.objects.all().filter(product_type='t-shirt',gender='F',category='womens')
    elif 'product/womens/clothing/jeans' in request.path:
        products = Products.objects.all().filter(product_type='jenas',gender='F',category='womens')
    elif 'product/womens/clothing/trousers' in request.path:
        products = Products.objects.all().filter(product_type='trousers',gender='F',category='womens')
    
    #kids section
    elif 'product/kids/clothing/shirts' in request.path:
        products = Products.objects.all().filter(product_type='shirt',category='kids')
    elif 'product/kids/clothing/t-shirts' in request.path:
        products = Products.objects.all().filter(product_type='t-shirt',category='kids')
    elif 'product/kids/clothing/jeans' in request.path:
        products = Products.objects.all().filter(product_type='jenas',category='kids')
    elif 'product/kids/clothing/trousers' in request.path:
        products = Products.objects.all().filter(product_type='trousers',category='kids')
    
    context = {
        'products':products,
    }
    return render(request,'shop/products.html',context)

#footwear products view function
def footwear(request):
    if 'product/mens/footwear/formals' in request.path:
        products = Products.objects.all().filter(product_type='formal',gender='M',category='Mens')
    elif 'product/mens/footwear/sports' in request.path:
        products = Products.objects.all().filter(product_type='sports',gender='M',category='Mens')
    elif 'product/mens/footwear/casuals' in request.path:
        products = Products.objects.all().filter(product_type='casual',gender='M',category='Mens')
    elif 'product/mens/footwear/sandals' in request.path:
        products = Products.objects.all().filter(product_type='sandal',gender='M',category='Mens')
    elif 'product/mens/footwear/sleepers' in request.path:
        products = Products.objects.all().filter(product_type='sleeper',gender='M',category='Mens')

    #women Section
    elif 'product/womens/footwear/formals' in request.path:
        products = Products.objects.all().filter(product_type='formal',gender='F',category='womens')
    elif 'product/womens/footwear/sports' in request.path:
        products = Products.objects.all().filter(product_type='sports',gender='F',category='woFens')
    elif 'product/womens/footwear/casuals' in request.path:
        products = Products.objects.all().filter(product_type='casual',gender='F',category='womens')
    elif 'product/womens/footwear/sandals' in request.path:
        products = Products.objects.all().filter(product_type='sandal',gender='F',category='womens')
    
    elif 'product/womens/footwear/sleepers' in request.path:
        products = Products.objects.all().filter(product_type='sleeper',gender='F',category='womens')        
    
    #kids section
    elif 'product/kids/footwear/formals' in request.path:
        products = Products.objects.all().filter(product_type='formal',category='kids')
    elif 'product/kids/footwear/sports' in request.path:
        products = Products.objects.all().filter(product_type='sports',category='kids')
    elif 'product/kids/footwear/casuals' in request.path:
        products = Products.objects.all().filter(product_type='casual',category='kids')
    elif 'product/kids/footwear/sandals' in request.path:
        products = Products.objects.all().filter(product_type='sandal',category='kids')
    elif 'product/kids/footwear/sleepers' in request.path:
        products = Products.objects.all().filter(product_type='sleeper',category='kids')   
    context = {
        'products':products,
    }
    return render(request,'shop/products.html',context)

#bags products page view function

def bags(request):

    #mens
    if 'product/men/bags/backpack' in request.path:
        products = Products.objects.all().filter(product_type='backpack',gender='M',category='Mens')
    elif 'product/men/bags/handbags' in request.path:
        products = Products.objects.all().filter(product_type='hand_bag',gender='M',category='Mens')
    elif 'product/men/bags/hobobags' in request.path:
        products = Products.objects.all().filter(product_type='hobo_bag',gender='M',category='Mens')
    elif 'product/men/bags/messengerbags' in request.path:
        products = Products.objects.all().filter(product_type='messenger_bag',gender='M',category='Mens')
    elif 'product/men/bags/shoulderbags' in request.path:
        products = Products.objects.all().filter(product_type='shoulder_bag',gender='M',category='Mens')
    elif 'product/men/bags/travellingbags' in request.path:
        products = Products.objects.all().filter(product_type='travelling_bag',gender='M',category='Mens')
    
    #womens
    if 'product/women/bags/backpack' in request.path:
        products = Products.objects.all().filter(product_type='backpack',gender='F',category='womens')
    elif 'product/women/bags/handbags' in request.path:
        products = Products.objects.all().filter(product_type='hand_bag',gender='F',category='womens')
    elif 'product/women/bags/hobobags' in request.path:
        products = Products.objects.all().filter(product_type='hobo_bag',gender='F',category='womens')
    elif 'product/women/bags/messengerbags' in request.path:
        products = Products.objects.all().filter(product_type='messenger_bag',gender='F',category='womens')
    elif 'product/women/bags/shoulderbags' in request.path:
        products = Products.objects.all().filter(product_type='shoulder_bag',gender='F',category='womens')
    elif 'product/women/bags/travellingbags' in request.path:
        products = Products.objects.all().filter(product_type='travelling_bag',gender='F',category='womens')

    #kids
    if 'product/kids/bags/backpack' in request.path:
        products = Products.objects.all().filter(product_type='backpack',category='kids')
    elif 'product/kids/bags/handbags' in request.path:
        products = Products.objects.all().filter(product_type='hand_bag',category='kids')
    elif 'product/kids/bags/hobobags' in request.path:
        products = Products.objects.all().filter(product_type='hobo_bag',category='kids')
    elif 'product/kids/bags/messengerbags' in request.path:
        products = Products.objects.all().filter(product_type='messenger_bag',category='kids')
    elif 'product/kids/bags/shoulderbags' in request.path:
        products = Products.objects.all().filter(product_type='shoulder_bag',category='kids')
    elif 'product/kids/bags/travellingbags' in request.path:
        products = Products.objects.all().filter(product_type='travelling_bag',category='kids')
    
    context = {
        'products':products,
    }
    return render(request,'shop/products.html',context)

def product_details(request,pk):
    product = Products.objects.get(pk=pk)
    if request.method == 'POST':
        user_id = request.user.id
        products_id  = product.id
        cart = Cart(products_id = products_id,user_id = user_id)
        cart.save()
    context={
        'product':product,
    } 

    return render(request,'products_details/product_details.html',context)
