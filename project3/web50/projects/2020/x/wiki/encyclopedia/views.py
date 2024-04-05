from django.shortcuts import render

from . import util

import markdown2


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
    