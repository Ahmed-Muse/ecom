from django.shortcuts import render, redirect
from .models import * #you can do dot because models and views are in the same directory as dot means from this directory
from django.http import JsonResponse
import json
import datetime
from .utils import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages#for flash messages
from django.http import HttpResponse# this is necessary for generating text files

from django.core.paginator import Paginator#this is important for the pagination
# Create your views here.
from systemadmins.decorators import *
import csv# stands for comma separated values

#start of libraries for generating pdf files
#BELOW IS FOR GENERATING PDFS
#pip install reportlab
from django.http import FileResponse
import io#this is input output
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#end of files for generating pdf files

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

@login_required#this is the decorator to ensure user is logged in to see this view
#@allowed_users(allowed_roles=['admin'])# this page will be seen by only the admins ....this docorator is from the systemadmins app...you can also add other lists
#@login_required(login_url='loginpage')
#@admin_only
def dashboard(request):
    
    context = {
        
    }

    return render(request,'dashboard.html',context)

def base_dashboard(request):
    
    context = {
        
    }

    return render(request,'base_dashboard.html',context)
#@allowed_users(allowed_roles=['admin'])
def hrm(request):
    
    context = {
        
    }

    return render(request,'ems/hrm/hrm.html',context)
@allowed_users(allowed_roles=['admin'])
#@admin_only
def stock(request):
    title="Physical Stock "
    header="Inventory Management System"
    form =AddPhysicalProductForm(request.POST or None)
    form_about_phys_items=AboutPhysicalItemsForm(request.POST or None)
    physical_products=PhysicalStockTable.objects.all().order_by('description')
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Stock added successfully')
        form=AddPhysicalProductForm()#this clears out the form after adding the product
    else:
       form.non_field_errors
    
        #start of the search form part.............................
        #search_form = SearchPhysicalItemsForm(request.POST or None)#this is for the search
        #if request.method == 'POST':
    	#query_table_content = SearchPhysicalItemsForm.objects.filter(part_number__icontains=form['part_number'].value(),
		#							description__icontains=form['description'].value())
        #End of search 
    
    #start of the pagination setup
    #import pagination library up, then do code below, then pass it to the templates
    pagination=Paginator(PhysicalStockTable.objects.all(),7)
    page=request.GET.get('page')#keep track of the pagination - each time you click, you need to know the page
    physical_products=pagination.get_page(page)#now this puts all together
    #next, pass this to the templates page (physical_products)

    #create a string that is equal to the number of pages in terms of its characters...like if page has 5 pages, then ahmed has the same
    page_num="a"*physical_products.paginator.num_pages

    #end of the pagination setup
        

    context = {
        "title":title,
        "form":form,
        "physical_products":physical_products,
        "header":header,
        "page_num":page_num,
        
        "form_about_phys_items":form_about_phys_items,
      
        
    }

    return render(request,'ems/stock/stock.html',context)


#@allowed_users(allowed_roles=['admin'])  
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
#@allowed_users(allowed_roles=['admin'])
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
    return render(request, 'ems/stock/update_physical_stock.html', context)#this is the main page rendered first

def product_list_text_file(request):
    response=HttpResponse(content_type='text/plain')#this means that instead of returning a page, return a text file
    response['Content-Disposition']='attachment; filename=products.txt'
    #now designate the model
    products=PhysicalStockTable.objects.all()
    #now loop through the list and output
    #writer = csv.writer(response)#this is showing error so comments out all
    #writer.writerow(['PART_NUMBER', 'DESCRIPTION', 'QUANTITY_IN_STORE','PRICE','COMMENTS'])
    #products.description.writerow(['PART_NUMBER', 'DESCRIPTION', 'QUANTITY_IN_STORE','PRICE','COMMENTS'])
    product_lines=[]#create an empty list
    for product in products:
        product_lines.append(f'{product.description}  {product.quantity} {product.price}\n')
    response.writelines(product_lines)
    return response

def product_list_csv(request):
    response=HttpResponse(content_type='text/csv')#this means that instead of returning a page, return a text file
    response['Content-Disposition']='attachment; filename=products.csv'
    #now designate the model
    products=PhysicalStockTable.objects.all()
    #create csv writer
    writer = csv.writer(response)#this writes to the file
    #add column headings to the csv file
    writer.writerow(['DESCRIPTION', 'QUANTITY','PRICE'])
    #products.description.writerow(['PART_NUMBER', 'DESCRIPTION', 'QUANTITY_IN_STORE','PRICE','COMMENTS'])
   
    for product in products:
        writer.writerow([product.description, product.quantity, product.price])
    
    return response

def product_list_pdf(request):
    #create bytestream buffer
    buf=io.BytesIO()
    #create canvas
    canv=canvas.Canvas(buf, pagesize=letter, bottomup=0)#letter sized regular paper size

    #create a text object
    textob=canv.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont('Helvetica',14)
    products=PhysicalStockTable.objects.all()

    product_lines=[]#create an empty list
    str(product_lines.append('Description'))+str(product_lines.append('Quantity'))
    for product in products:
        #product_lines.append(f'{product.description} {product.quantity} {product.price} \n')
        product_lines.append(product.description)
        product_lines.append(product.quantity)
        product_lines.append(product.price)
        product_lines.append('................')
 
    #loop through
    for product_line in product_lines:
        #textob.textLine(product_line) this gave errors
        textob.textLine(str(product_line))
    canv.drawText(textob)
    canv.showPage()
    canv.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True,filename='product.pdf')

    #add some lines of text

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

def search_physical_items(request):
    search_return=PhysicalStockTable.objects.all()
    search_form=SearchPhysicalItemsForm(request.POST or None)
    if request.method == 'POST':
        search_return = PhysicalStockTable.objects.filter(part_number__icontains=search_form['part_number'].value(),
								description__icontains=search_form['description'].value())
      
    
    
   
    context={
        "search_form":search_form,
        "search_return":search_return,
        
        
    }
    return render(request,"ems/stock/search_physical_items.html",context)



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
    form=AddPhysicalProductForm(request.POST or None)
    products = PhysicalStockTable.objects.all()
    
   
    context={
        "title": title,
        "form":form,
        "products":products,
        

       
        
        }
    return render(request,'test.html',context)

def language(request):
    languages = Language.objects.all()
    physical_products=PhysicalStockTable.objects.all()
    return render(request,'language.html',{"languages":languages,"product":physical_products})