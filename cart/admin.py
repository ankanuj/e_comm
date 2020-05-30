from django.contrib import admin

from .models import *

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'products','user')
    list_display_links = ('id', 'products','user')
    list_filter = ('products',)
    list_per_page =  25
    search_fields = ('products',)

admin.site.register(Cart,CartAdmin)
