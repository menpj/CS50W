from django.shortcuts import render

from . import util

from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

import markdown2

import re


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#def content(request):
def wiki(request,name):
    #name=request.GET.get('name')
    entryBody=util.get_entry(name)


    if entryBody:
        entryBody= markdown2.markdown(entryBody)
        file1 = open(f"encyclopedia/templates/wiki/{name}.html","w")
        
        file1.write(entryBody)
        file1.close()
        return render(request, f"wiki/{name}.html")
    else:
        return render(request, "encyclopedia/content.html", {
            "content": None
        })
    

def wikiSearch(request):

    if request.method=="POST":
        name=request.POST['q']
        entryBody=util.get_entry(name)
        if entryBody:
            entryBody= markdown2.markdown(entryBody)
            file1 = open(f"encyclopedia/templates/wiki/{name}.html","w")
            
            file1.write(entryBody)
            file1.close()
            #return render(request, f"wiki/{name}.html")
            return HttpResponseRedirect(f"wiki/{name}")
        else:
            entryList=util.list_entries()
            matchEntryList = []
            for entry in entryList:
                match= re.search(name,entry,re.I)
                if match:
                    matchEntryList.append(entry)
                else:
                    pass
                    #matchEntryList.append(entry)

            #print(matchEntryList)
            if matchEntryList:
                return render(request, "encyclopedia/search.html", {
                    "entries": matchEntryList
                })
            else:

                return render(request, "encyclopedia/content.html", {
                    "content": None
            })    
    

class NewTaskForm(forms.Form):
    title=forms.CharField(label="New Page Title",empty_value="Page Title",max_length=100)
    body=forms.CharField(label="Page Body",widget=forms.Textarea)
    #priority = forms.IntegerField(label="Priority",min_value=1,max_value=10)

def newPage(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            body=form.cleaned_data["body"]
            print(title)
            print(body)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request,"encyclopedia/newpage.html",{
                "form":form
            })
    return render(request, "encyclopedia/newpage.html",{"form": NewTaskForm()}) 

