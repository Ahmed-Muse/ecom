import json
from .models import *
def cookieCart(request):
    try:
        cart=json.loads(request.COOKIES['cart'])#this will turn back to python dictionary
    except:
        cart={}
    print('Cart:',cart)
    items=[]
    order={'get_cart_total':0, 'get_cart_items':0,'shipping':False}#this is to avoid error for unauthenticated user, when you log out
    cartItems= order['get_cart_items']
    for i in cart:
        try:
            cartItems+=cart[i]['quantity']
            product=Product.objects.get(id=i)
            total=(product.price * cart[i]['quantity'])
            order['get_cart_total']+=total
            order['get_cart_items']+=cart[i]['quantity']
            item={
                'product':{
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'imageURL':product.imageURL,
                 },
                'quantity':cart[i]['quantity'],
                'get_total':total
                }
            items.append(item)
            if product.digital==False:
                order['shipping']=True
        except:
            pass
    return {'cartItems':cartItems,'order':order,'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        #either create or find the order... below is two functions combined...to understand better, check docs of _or_create django
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        
        #then get the items attached to that order
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        cookieData=cookieCart(request)
        cartItems=cookieData['cartItems']
        order=cookieData['order']
        items=cookieData['items']
        ''' items=[]
        
        order={'get_cart_total':0, 'get_cart_items':0,'shipping':False}#this is to avoid error for unauthenticated user, when you log out
        cartItems=order['get_cart_items'] '''
    return {'cartItems':cartItems,'order':order,'items':items}

def guestOrder(request, data):
    print("User is not logged in !")
    print('COOKIES:',request.COOKIES)
    name=data['form']['name']
    email=data['form']['email']
    cookieData=cookieCart(request)
    items=cookieData['items']
    customer, created=Customer.objects.get_or_create(
        email=email,
        )
    customer.name=name
    customer.save()
    order=Order.objects.create(
        customer=customer, 
        complete=False,
        )
    for item in items:
        product=Product.objects.get(id=item['product']['id'])
        orderItem=OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
            )
    return customer, order