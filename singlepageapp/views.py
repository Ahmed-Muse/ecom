from django.shortcuts import render

# Create your views here.
def index(request):
    title="testing"
    return render(request,'singleapp/index.html', {"title":title})