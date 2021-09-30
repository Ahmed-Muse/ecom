from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customerpdf(models.Model):
    customer_name=models.CharField(max_length=200)#pip install pillow
    logo=models.ImageField()
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.customer_name

class Postpdf(models.Model):
    title=models.CharField(max_length=200)

    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    def __str__(self):
        return self.title
class Logopdf(models.Model):
    company_name=models.CharField(max_length=50)
    logo=models.ImageField()
    def __str__(self):
        return self.company_name
    