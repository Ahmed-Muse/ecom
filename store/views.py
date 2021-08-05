from django.shortcuts import render
from .models import * #you can do dot because models and views are in the same directory as dot means from this directory
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def store(request):
    title="Allifmaal System"
    if request.user.is_authenticated:
        customer=request.user.customer
        #either create or find the order... below is two functions combined...to understand better, check docs of _or_create django
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0,'shipping':False}
        cartItems=['get_cart_items']
    products = Product.objects.all()#assign all the objects in the table to the variable

    context = {
	"title": title,
    "cartItems":cartItems,
    #"query_ProductTable_content":query_ProductTable_content,
    "products": products,
	}#context contains the number of variables to be passed/called to the html templates/pages
    #so basically we are telling the views to pass whatever is contained in the context to the index.html page.

    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        #either create or find the order... below is two functions combined...to understand better, check docs of _or_create django
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        
        #then get the items attached to that order
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0,'shipping':False}#this is to avoid error for unauthenticated user, when you log out
        cartItems=['get_cart_items']
    context={
        "items":items,
        "order":order,
        "cartItems":cartItems,
    }
    return render(request, 'store/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        #either create or find the order... below is two functions combined...to understand better, check docs of _or_create django
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        
        #then get the items attached to that order
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        
        order={'get_cart_total':0, 'get_cart_items':0,'shipping':False}#this is to avoid error for unauthenticated user, when you log out
        cartItems=['get_cart_items']
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
    else:
        print("User is not logged in !")
    return JsonResponse('Payment complete...', safe=False)