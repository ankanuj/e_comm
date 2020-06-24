from django.shortcuts import render,redirect
from django.views import View
from products.models import *
from django.contrib import messages

def shop(request):
    return render(request,'shop/shop.html')

def men_shop(request):
    return render(request,'shop/mens.html')

def women_shop(request):
    return render(request,'shop/womens.html')

def kids_shop(request):
    return render(request,'shop/kids.html')

def mens_clothing(request):
    return render(request,'shop/clothing.html')

def womens_clothing(request):
    return render(request,'shop/w_clothing.html')
def kids_clothing(request):
    return render(request,'shop/k_clothing.html')

#footwear
def mens_footwear(request):
    return render(request,'shop/footwear.html')

def womens_footwear(request):
    return render(request,'shop/w_footwear.html')

def kids_footwear(request):
    return render(request,'shop/k_footwear.html')

#watches
def m_watches(request):
    return render(request,'shop/watches.html')
def k_watches(request):
    return render(request,'shop/k_watches.html')
def w_watches(request):
    return render(request,'shop/w_watches.html')

#bags
def mens_bags(request): 
    return render(request,'shop/bags.html')
def womens_bags(request): 
    return render(request,'shop/w_bags.html')  
def kids_bags(request): 
    return render(request,'shop/kids_bags.html')                    
    

'''
def electronics_shop(request):
    return render(request,'shop/electronics.html')

def beauty_shop(request):
    return render(request,'shop/beauty_products.html')

def other_shop(request):
    return render(request,'shop/other_stuff.html')
'''
