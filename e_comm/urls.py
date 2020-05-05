from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main_app.urls')),
    path('/',include('register.urls')),
    path('accounts/',include('accounts.urls')),
    path('shops/',include('shop.urls')),
    path('accounts/',include('allauth.urls')),
    path('accounts/',include('allauth.urls')),
    path('accounts/',include('cart.urls')),
    path('shops/',include('products.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
