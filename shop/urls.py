from django.urls import path
from . import views
urlpatterns = [
    path('',views.shop,name='shops'),
    path('mens/',views.men_shop,name='mens'),
    path('women/',views.women_shop,name='women'),
    path('kids/',views.kids_shop,name='kids'),
    


    path('mens/footwear/',views.mens_footwear,name='footwear_men'),
    path('womens/footwear/',views.womens_footwear,name='women_footwear'),
    path('kids/footwear/',views.kids_footwear,name='kids_footwear'),

    path('mens/watches/',views.m_watches,name='m_watches'),
    path('womens/watches/',views.w_watches,name='w_watches'),
    path('kids/watches/',views.k_watches,name='k_watches'),

    path('bags/mens',views.mens_bags,name='men_bags'),
    path('bags/womens',views.womens_bags,name='women_bags'),
    path('bags/kids',views.kids_bags,name='kids_bags'),


    path('mens/clothing/',views.mens_clothing,name='clothing_mens'),
    path('womens/clothing/',views.womens_clothing,name='clothing_womens'),
    path('kids/clothing/',views.kids_clothing,name='clothing_kids'),


    
]   