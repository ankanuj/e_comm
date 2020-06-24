from django.urls import path
from . import views
urlpatterns = [
    path('product/mens/clothing/shirts',views.products,name='products'),
    path('product/mens/clothing/t-shirts',views.products,name='products_t-shirts'),
    path('product/mens/clothing/jeans',views.products,name='products_jeans'),
    path('product/mens/clothing/trousers',views.products,name='products_trousers'),
#women clothing urls   
    path('product/womens/clothing/shirts',views.products,name='products_women'),
    path('product/womens/clothing/t-shirts',views.products,name='products_women_t-shirts'),
    path('product/womens/clothing/jeans',views.products,name='products_women_jeans'),
    path('product/womens/clothing/trousers',views.products,name='products_women_trousers'),
#kids clothing urls
    path('product/kids/clothing/shirts',views.products,name='products_kids_shirts'),
    path('product/kids/clothing/t-shirts',views.products,name='products_kids_t-shirts'),
    path('product/kids/clothing/jeans',views.products,name='products_kids_jeans'),
    path('product/kids/clothing/trousers',views.products,name='products_kids_trousers'),
#mens footwear urls
    path('product/mens/footwear/formals',views.footwear,name='formals_men'),
    path('product/mens/footwear/sports',views.footwear,name='sports_men'),
    path('product/mens/footwear/casuals',views.footwear,name='casuals_men'),
    path('product/mens/footwear/sandals',views.footwear,name='sandals_men'),
    path('product/mens/footwear/sleepers',views.footwear,name='sleepers_men'),
#women footwear urls
    path('product/womens/footwear/formals',views.footwear,name='formals_women'),
    path('product/womens/footwear/sports',views.footwear,name='sports_women'),
    path('product/womens/footwear/casuals',views.footwear,name='casuals_women'),
    path('product/womens/footwear/sandals',views.footwear,name='sandals_women'),
    path('product/womens/footwear/sleepers',views.footwear,name='sleepers_women'),      
#kids footwear urls
    path('product/kids/footwear/formals',views.footwear,name='formals_kids'),
    path('product/kids/footwear/sports',views.footwear,name='sports_kids'),
    path('product/kids/footwear/casuals',views.footwear,name='casuals_kids'),
    path('product/kids/footwear/sandals',views.footwear,name='sandals_kids'),
    path('product/kids/footwear/sleepers',views.footwear,name='sleepers_kids'),

#Bags Urls
    path('product/men/bags/backpack',views.bags,name='backpack_men'),
    path('product/men/bags/handbags',views.bags,name='handbags_men'),
    path('product/men/bags/hobobags',views.bags,name='hobobags_men'),
    path('product/men/bags/shoulderbags',views.bags,name='shoulderbags_men'),
    path('product/men/bags/messengerbags',views.bags,name='messengerbags_men'),
    path('product/men/bags/travellingbags',views.bags,name='travellingbags_men'),

    #women
    path('product/women/bags/backpack',views.bags,name='backpack_women'),
    path('product/women/bags/handbags',views.bags,name='handbags_women'),
    path('product/women/bags/hobobags',views.bags,name='hobobags_women'),
    path('product/women/bags/shoulderbags',views.bags,name='shoulderbags_women'),
    path('product/women/bags/messengerbags',views.bags,name='messengerbags_women'),
    path('product/women/bags/travellingbags',views.bags,name='travellingbags_women'),

    #kids
    path('product/kids/bags/backpack',views.bags,name='backpack_kids'),
    path('product/kids/bags/handbags',views.bags,name='handbags_kids'),
    path('product/kids/bags/hobobags',views.bags,name='hobobags_kids'),
    path('product/kids/bags/shoulderbags',views.bags,name='shoulderbags_kids'),
    path('product/kids/bags/messengerbags',views.bags,name='messengerbags_kids'),
    path('product/kids/bags/travellingbags',views.bags,name='travellingbags_kids'),


    path('product/mens/watches/digital',views.watches,name='m_digital'),
    path('product/mens/watches/analog',views.watches,name='m_analog'),
    path('product/mens/watches/hybrid',views.watches,name='m_hybrid'),
    path('product/mens/watches/smart/band',views.watches,name='m_smart_band'),
  
    path('product/womens/watches/digital',views.watches,name='w_digital'),
    path('product/womens/watches/analog',views.watches,name='w_analog'),
    path('product/womens/watches/hybrid',views.watches,name='w_hybrid'),
    path('product/womens/watches/smart/band',views.watches,name='w_smart_band'),

    path('product/kids/watches/digital',views.watches,name='k_digital'),
    path('product/kids/watches/analog',views.watches,name='k_analog'),
    path('product/kids/watches/hybrid',views.watches,name='k_hybrid'),
    path('product/kids/watches/smart/band',views.watches,name='k_smart_band'),



    
    path('product/clothing/{?P<pk>\d+}',views.product_details,name='product_clothing_details'),
    path('product/footwear/{?P<pk>\d+}',views.product_details,name='product_footwear_details'),
    path('product/bags/{?P<pk>\d+}',views.product_details,name='product_bags_details'),
    path('product/watches/{?P<pk>\d+}',views.product_details,name='product_watches_details'),



]