from django.shortcuts import render
from django.http import Http404,HttpResponse

# Create your views here.
def index(request):
    title="testing"
    return render(request,'singleapp/index.html', {"title":title})

texts=["This is page 1","This is page 3","This is page 3"]
# Create your views here.
def index2(request):
    title="testing"
    return render(request,'singleapp/singlepageappwithurl.html', {"title":title})

texts=["This is page 1","This is page 3","This is page 3"]

def section(request,num):
    if 1<=num<=3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404(" no such section")
    #return render(request,'singleapp/singlepageappwithurl.html')

