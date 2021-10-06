from django.db import models


# Create your models here.

class TasksModel(models.Model):
   
    task_status = [
    ('complete', 'complete'),
    ('incomplete', 'incomplete'),
    
    ]

    title = models.CharField(max_length=200, null=True)
    task = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=task_status,default='incomplete')
    createDate=models.DateTimeField(auto_now_add=True)
    dueDate=models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    complete=models.BooleanField(default=False)
    
    
    
    def __str__(self):
    		return self.title