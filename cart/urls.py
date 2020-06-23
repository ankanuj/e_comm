from django.urls import path
from . import views

urlpatterns = [
    path('shops/cart/',views.cart,name='cart'),
    path('shops/cart/address',views.address,name='address'),
    path('shops/cart/place-order',views.order,name='order'),
    path('shops/cart/place-order/payment_handle',views.paymenthandle,name='payment'),


]