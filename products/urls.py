from django.urls import path
from . import views
urlpatterns = [
    path('product/mens/shirts',views.products,name='products'),
    path('product/mens/t-shirts',views.products,name='products_t-shirts'),
    path('product/mens/jeans',views.products,name='products_jeans'),
    path('product/mens/trousers',views.products,name='products_trousers'),
    
    path('product/womens/shirts',views.products,name='products_women'),
    path('product/womens/t-shirts',views.products,name='products_women_t-shirts'),
    path('product/womens/jeans',views.products,name='products_women_jeans'),
    path('product/womens/trousers',views.products,name='products_women_trousers'),

    path('product/kids/shirts',views.products,name='products_kids_shirts'),
    path('product/kids/t-shirts',views.products,name='products_kids_t-shirts'),
    path('product/kids/jeans',views.products,name='products_kids_jeans'),
    path('product/kids/trousers',views.products,name='products_kids_trousers'),

    path('product/{?P<pk>\d+}',views.product_details,name='product_details'),
]