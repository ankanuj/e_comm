from django.urls import path
from . import views

urlpatterns = [
    path('shops/cart/',views.cart,name='cart'),
]