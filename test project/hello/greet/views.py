from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html",{"entry":"kundi"})
    #return HttpResponse("Hello, Noah!")
    #return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
def noah(request):
    return HttpResponse("Hello, Noah!")

def david(request):
    return HttpResponse("Hello, David!")

def hello(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})

   
