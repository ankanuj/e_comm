from django.urls import path
from . import views
urlpatterns = [
    path('',views.shop,name='shops'),
    path('mens/',views.men_shop,name='mens'),
    path('women/',views.women_shop,name='women'),
    path('kids/',views.kids_shop,name='kids'),
    #path('electronics/',views.electronics_shop,name='electronics'),
    #path('beauty_products/',views.beauty_shop,name='beauty'),
    #path('other_stuff/',views.other_shop,name='other'),


    path('mens/footwear/',views.footwear,name='footwear_men'),
    path('womens/footwear/',views.footwear,name='women_footwear'),
    path('kids/footwear/',views.footwear,name='kids_footwear'),

    path('mens/watches/',views.watches,name='men_watches'),
    path('womens/watches/',views.watches,name='women_watches'),
    path('kids/watches/',views.watches,name='kids_watches'),

    path('bags/mens',views.mens_bags,name='men_bags'),
    path('bags/womens',views.womens_bags,name='women_bags'),
    path('bags/kids',views.kids_bags,name='kids_bags'),


    path('mens/clothing/',views.clothing,name='clothing_mens'),
    path('womens/clothing/',views.clothing,name='clothing_womens'),
    path('kids/clothing/',views.clothing,name='clothing_kids'),


    
]   