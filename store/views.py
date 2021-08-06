from django.shortcuts import render
from .models import * #you can do dot because models and views are in the same directory as dot means from this directory
from django.http import JsonResponse
import json
import datetime
from .utils import *
# Create your views here.

def store(request):
    data=cartData(request)
    cartItems=data['cartItems']
    
    products = Product.objects.all()#assign all the objects in the table to the variable

    context = {
	
    "cartItems":cartItems,
    "data":data,
    #"query_ProductTable_content":query_ProductTable_content,
    "products": products,
	}#context contains the number of variables to be passed/called to the html templates/pages
    #so basically we are telling the views to pass whatever is contained in the context to the index.html page.

    return render(request,'store/store.html',context)

def cart(request):
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    context={
        "items":items,
        "order":order,
        "cartItems":cartItems,
    }
    return render(request, 'store/cart.html', context)
def checkout(request):
    
    data=cartData(request)
    cartItems=data['cartItems']
    order=data['order']
    items=data['items']
    context={
        "items":items,
        "order":order,
        "cartItems":cartItems,
    }
    
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data=json.loads(request.body)
    #data=json.loads(request.data)
    productId=data['productId']
    action=data['action']
    print('Action:',action)
    print('ProductId:',productId)
    
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order, created=Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created=OrderItem.objects.get_or_create(order=order,product=product)
    
    
    if action=='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
        
    
      
    return JsonResponse("item added", safe=False)

def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        
        
    else:
        customer, order= guestOrder(request, data)
        
    
    #regardless of user, ensure you can below data and that we have order object for both users, authenticated and unauthenticated
    total=float(data['form']['total'])
    order.transaction_id=transaction_id
    if total ==order.get_cart_total:
        order.complete=True
    order.save()
    if order.shipping==True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
                
            )
    
    return JsonResponse('Payment complete...', safe=False)