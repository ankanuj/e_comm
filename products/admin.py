from django.contrib import admin
from .models import *

class ClothingAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name','category','product_type','size', 'gender','price','is_published')
    list_display_links = ('id', 'brand_name','is_published')
    list_filter = ('brand_name','category','product_type','gender','is_published')
    list_per_page =  25
    search_fields = ('brand_name','product_type','category',)

admin.site.register(Clothing,ClothingAdmin)

class FootwearAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name','category','product_type','size', 'gender','price','is_published')
    list_display_links = ('id', 'brand_name','is_published')
    list_filter = ('brand_name','category','product_type','gender','is_published')
    list_per_page =  25
    search_fields = ('brand_name','product_type','category',)

admin.site.register(Footwear,FootwearAdmin)

class BagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name','category','product_type', 'gender','price','is_published')
    list_display_links = ('id', 'brand_name','is_published')
    list_filter = ('brand_name','category','product_type','gender','is_published')
    list_per_page =  25
    search_fields = ('brand_name','product_type','category',)

admin.site.register(Bags,BagsAdmin)