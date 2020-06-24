from django.shortcuts import render,redirect
from products.models import *
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
from payment_gateway import Checksum
MERCHANT_KEY = 'G6ve7i3Y_5khbGfI'


def  cart(request):
    cart = Cart.objects.all().filter(user_id = request.user.id)
    price=Cart.objects.all().filter(user_id = request.user.id)
    address = Address.objects.all().filter(user_id = request.user.id)

    total_price = 0
    for price in price:
        total_price = total_price + price.products.price
    context = {
        'cart':cart,
        'total_price':total_price,
        'address':address,
    }
    if request.method == "POST":
        item = request.POST['item']
        remove = Cart.objects.get(pk=item)
        remove.delete()
        return render(request,'cart/cart.html',context)
    
    return render(request,'cart/cart.html',context)

def address(request):
    cart = Cart.objects.all()
   
    context = {
        'cart':cart,
        
    }

    if request.method == "POST":
        user_id = request.user.id
        address = request.POST['address']
        district = request.POST['district']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        mobile = request.POST['mobile']

        deliever = Address(user_id = user_id, address=address, state = state, district = district, zipcode=zipcode, mobile =mobile )
        deliever.save()
        return redirect('cart')


    return render(request,'cart/address.html')



def order(request):
    cart = Cart.objects.all().filter(user_id = request.user.id)
    email = request.user.email
    price=Cart.objects.all().filter(user_id = request.user.id)
    address = Address.objects.all().filter(user_id = request.user.id)

    total_price = 0
    for price in price:
        total_price = total_price + price.products.price

    context = {
        'cart':cart,
        'total_price':total_price,
        'address':address,
            }

    if request.method == 'POST':
        address_id = request.POST['address']
        user_id = request.user.id
        product = request.POST['product']
        amount = total_price
        order_details = Order(user_id = user_id,address_id = address_id, amount = amount,product_id = product)
        order_details.save()
        order_id = order_details.id

        #now request payment method to accept the payment by the user and transfer to your account
        data_dict = {
            'MID':'XEljrT93681832887767',
            'ORDER_ID':str(order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/accounts/shops/cart/place-order/payment_handle',
        }
        data_dict['CHECKSUMHASH'] =Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request,'cart/payment.html',{'data_dict':data_dict})
    
    return render(request,'cart/order.html',context)

@csrf_exempt
def paymenthandle(request):
    #accept post request by the payment gateway
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    
    verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY, checksum )
    if verify:
        if response_dict['RESPCODE'] == '01':
           
            order_id = response_dict['ORDERID']
            trsn_id = response_dict['TXNID']
            trsn_date = response_dict['TXNDATE']
            trsn_amount = response_dict['TXNAMOUNT']
            trsn_status = response_dict['STATUS']

            payment_details = PaymentDetails( order_id = order_id, trsn_amount = trsn_amount,
                                            trsn_date= trsn_date,trsn_id = trsn_id, trsn_status = trsn_status)
            payment_details.save()
        else:
            message.error(request,"something went wrong can't proceed, if money get deducted it will be refunded soon. ")
    return render(request,'cart/paymentstatus.html',{'response':response_dict})