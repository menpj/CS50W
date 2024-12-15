from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here
def index(request, path):
    return HttpResponse(f"Requested Path: {path}")
    #http://127.0.0.1:8000/%3Cscript%3Ealert(%22Hello!%22);%3C/script%3E is an example of cross site scripting
