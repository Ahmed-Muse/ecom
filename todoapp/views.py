from django.shortcuts import render,redirect
from .forms import *


def index(request):
   
    form =AddTasksForm(request.POST or None)
   
    tasks=TasksModel.objects.all()
    
    if form.is_valid():
        form.save()
        
        form=AddTasksForm()#this clears out the form after adding the product
    
        

    context = {
        "form":form,
        "tasks":tasks,
        
        
    }

    return render(request,'todoapp/index.html',context)


#@allowed_users(allowed_roles=['admin'])  
def delete_task(request,pk):
    delete_task=TasksModel.objects.get(id=pk)
    if request.method =="POST":
        
        delete_task.delete()
        
        return redirect('todoapp:index')
    context={
        "delete_task":delete_task,
    }
    return render(request,'todoapp/delete_task.html',context)

def update_tasks(request, pk):
    update_task= TasksModel.objects.get(id=pk)
    form = AddTasksForm(instance=  update_task)
   
    if request.method == 'POST':
        form = AddTasksForm(request.POST, instance=  update_task)
        if form.is_valid():
            form.save()
          
            return redirect('todoapp:index')#just redirection page
    context = {
		'form':form,
        " update_task": update_task,
    }
    return render(request, 'todoapp/update_tasks.html', context)#this is the main page rendered first