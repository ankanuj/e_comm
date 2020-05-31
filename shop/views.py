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

def clothing(request):
    return render(request,'shop/clothing.html')

def footwear(request):
    return render(request,'shop/footwear.html')

def watches(request):
    return render(request,'shop/watches.html')

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
