from django.contrib import admin

from .models import *

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'products','user',)
    list_display_links = ('id', 'products','user')
    list_filter = ('products',)
    list_per_page =  25
    search_fields = ('products',)

admin.site.register(Cart,CartAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'user','state','zipcode')
    list_display_links = ('id', 'user',)
    list_filter = ('user',)
admin.site.register(Address,AddressAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'address','user','amount')
    list_display_links = ('id','user')
    list_filter = ('user',)
    list_per_page = 25
admin.site.register(Order,OrderAdmin)

class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ('id','trsn_amount','order_id','trsn_date','trsn_id' )
    list_display_links = ('id','order_id')
    list_filter = ('order_id',)
    list_per_page = 25
admin.site.register(PaymentDetails,PaymentDetailAdmin)