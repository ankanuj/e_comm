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
    path('mens/footwear/',views.men_footwear,name='men_footwear'),
    path('mens/watches/',views.men_watches,name='men_watches'),
    path('mens/bags/',views.men_bags,name='men_bags'),

    path('mens/clothing/',views.clothing,name='clothing_mens'),
    path('womens/clothing/',views.clothing,name='clothing_womens'),
    path('kids/clothing/',views.clothing,name='clothing_kids'),


    
]   