from django.shortcuts import render
from .models import * #you can do dot because models and views are in the same directory as dot means from this directory

# Create your views here.

def store(request):
    title="Allifmaal System"
    products = Product.objects.all()#assign all the objects in the table to the variable

    context = {
	"title": title,
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
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}#this is to avoid error for unauthenticated user, when you log out
    context={
        "items":items,
        "order":order,
    }
    return render(request, 'store/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        #either create or find the order... below is two functions combined...to understand better, check docs of _or_create django
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        
        #then get the items attached to that order
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}#this is to avoid error for unauthenticated user, when you log out
    context={
        "items":items,
        "order":order,
    }
    
    return render(request, 'store/checkout.html', context)
