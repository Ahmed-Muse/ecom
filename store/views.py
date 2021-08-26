from django.shortcuts import render, redirect
from .models import * #you can do dot because models and views are in the same directory as dot means from this directory
from django.http import JsonResponse
import json
import datetime
from .utils import *
from .forms import *
from django.contrib import messages
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
def main(request):
    return render(request, 'store/main.html')

def website(request):
    
    context = {
        
    }

    return render(request,'website.html',context)
def dashboard(request):
    
    context = {
        
    }

    return render(request,'dashboard.html',context)

def base_dashboard(request):
    
    context = {
        
    }

    return render(request,'base_dashboard.html',context)
def hrm(request):
    
    context = {
        
    }

    return render(request,'ems/hrm/hrm.html',context)
def stock(request):
    title="Physical Stock "
    header="Inventory Management System"
    form =AddPhysicalProductForm(request.POST or None)
    form_test=AddProductForTestingOnlyForm(request.POST or None)
    form_about_phys_items=AboutPhysicalItemsForm(request.POST or None)
    physical_products=PhysicalStockTable.objects.all()
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Stock added successfully')
        form=AddPhysicalProductForm()#this clears out the form after adding the product
    else:
       form.non_field_errors
    
    """  # start of the search form part.............................
    form = AddPhysicalProductForm(request.POST or None)#this is for the search
    if request.method == 'POST':
    	query_table_content = AddPhysicalProductForm.objects.filter(part_number__icontains=form['part_number'].value(),
									description__icontains=form['description'].value())
     #End of search """

    context = {
        "title":title,
        "form":form,
        "physical_products":physical_products,
        "header":header,
        "form_test":form_test,
        "form_about_phys_items":form_about_phys_items,
        
    }

    return render(request,'ems/stock/stock.html',context)


    
def delete_physical_stock(request,pk):
    delete_table_content=PhysicalStockTable.objects.get(id=pk)
    if request.method =="POST":
        
        delete_table_content.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('stock')
    context={
        "delete_table_content":delete_table_content,
    }
    return render(request,'ems/stock/delete_physical_stock.html',context)

def update_physical_stock(request, pk):
    update_table_content= PhysicalStockTable.objects.get(id=pk)
    form = AddPhysicalProductForm(instance= update_table_content)#insert the content of the table stored in the selected id in the update form
    #we could have used the add customer form but the validation will refuse us to update since fields may exist
    if request.method == 'POST':
        form = AddPhysicalProductForm(request.POST, instance= update_table_content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock updated successfully')
            return redirect('/stock')#just redirection page
    context = {
		'form':form,
        "update_table_content":update_table_content,
    }
    return render(request, 'ems/stock/stock.html', context)#this is the main page rendered first


def customers(request):
    
    context = {
        
    }

    return render(request,'ems/customers/customers.html',context)

def issue_or_receive_physical_items(request, pk):
    header="Receive or issue items "
    query_table_content =PhysicalStockTable.objects.get(id=pk)

    context = {
        "header":header,

		"query_table_content": query_table_content,

	}
    return render(request, "ems/stock/issue_or_receive_physical_items.html", context)

def issue_physical_items(request, pk):
    query_table_content =PhysicalStockTable.objects.get(id=pk)
    form = IssuePhysicalItemsForm(request.POST or None, instance=query_table_content)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.received_quantity=0
        instance.quantity -= instance.issued_quantity
        #instance.line_total=instance.price*instance.quantity_in_store
        #instance.quantity=instance.quantity - instance.issue_quantity

        #instance.issue_by = str(request.user)
     
        instance.issued_by=str(request.user)
        instance.save()

        #return redirect('/stock'+str(instance.id))
        return redirect('/stock')
    context = {
		"title": 'Issue ' + str(query_table_content.part_number),
		"query_table_content": query_table_content,
		"form": form,
		#"username": 'Issue By: ' + str(request.user),
	}
    return render(request, "ems/stock/issue_or_receive_physical_items.html", context)
def receive_physical_items(request, pk):
    query_table_content = PhysicalStockTable.objects.get(id=pk)
    form = ReceivePhysicalItemsForm(request.POST or None, instance=query_table_content)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.issued_quantity=0
        instance.quantity +=instance.received_quantity
        instance.receive_by=str(request.user)
        instance.save()
    
       # return redirect('/stock_details/'+str(instance.id))
        return redirect('/stock/')
    context = {
			"title": 'Receive ' + str(query_table_content.part_number),
			"query_table_content": query_table_content,
			"form": form,
			#"username": 'Receive By: ' + str(request.user),
		}
    return render(request, "ems/stock/issue_or_receive_physical_items.html", context)

def reorder_level(request,pk):
    query_table_content =PhysicalStockTable.objects.get(id=pk)
    form=PhysicalItemsReorderLevelForm(request.POST or None,instance=query_table_content)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
      
        return redirect('/stock')
    context={
        "instance":query_table_content,
        "form":form,
    }
    return render(request,"ems/stock/stock.html",context)

def product_full_details(request,pk):
    query_table_content =PhysicalStockTable.objects.get(id=pk)
    
   
    context={
        "query_table_content":query_table_content,
        
    }
    return render(request,"ems/stock/product_full_details.html",context)



################# start .............online parts#########################################
def stock_online(request):
    title="Allifmaal Online Stock"
    form=AddOnlineStockForm(request.POST or None)
    items = Product.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('stock_online')
   
    context={
        "title": title,
        "form":form,
        "items":items,
        
        }
    return render(request,'store/stock_online.html',context)

def customer_online(request):
    title="Allifmaal Online Stock"
    form=AddOnlineCustomerForm(request.POST or None)
    customers = Customer.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('customer_online')
   
    context={
        "title": title,
        "form":form,
        "customers":customers,
        
        }
    return render(request,'store/customer_online.html',context)
def orders_online(request):
    title="Allifmaal Online Stock"
    form=AddOnlineOrdersForm(request.POST or None)
    orders = Order.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('orders_online')
   
    context={
        "title": title,
        "form":form,
        "orders":orders,
        
        }
    return render(request,'store/orders_online.html',context)

def order_online_items(request):
    title="Allifmaal Online Stock"
    form=OrderOnlineItemsForm(request.POST or None)
    orderitems = OrderItem.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('order_online_items')
   
    context={
        "title": title,
        "form":form,
        "orderitems":orderitems,
        
        }
    return render(request,'store/order_online_items.html',context)

def shipping_address_online(request):
    title="Allifmaal Online Stock"
    form=AddShippingAdressOnlineForm(request.POST or None)
    shipping_details = ShippingAddress.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('shipping_address_online')
   
    context={
        "title": title,
        "form":form,
        "shipping_details":shipping_details,
        
        }
    return render(request,'store/shipping_address_online.html',context)

################### end ............. online part####################################################


####################### below is for testing only
def test(request):
    title="Testing Page"
    form=AddProductForTestingOnlyForm(request.POST or None)
    products = ForTestingOnly.objects.all()
    
   
    context={
        "title": title,
        "form":form,
        "products":products,
        

       
        
        }
    return render(request,'test.html',context)