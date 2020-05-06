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
    

    path('product/clothing/{?P<pk>\d+}',views.product_details,name='product_clothing_details'),
    path('product/footwear/{?P<pk>\d+}',views.product_details,name='product_footwear_details'),

]