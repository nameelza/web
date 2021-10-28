from re import S
from django.shortcuts import render

from . import util

import markdown2
from random import random

def index(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Invalid request"
        })

def entry(request, title):
    if request.method == "GET":
        entry = util.get_entry(title)
        if entry:
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "entry": markdown2.markdown(entry)
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "Entry not found"
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Invalid request"
        })

def search(request):
    if request.method == "GET":
        query = request.GET.get("q").lower()
        entries = util.list_entries()
        results = []
        for ent in entries:
            if query == ent.lower():
                return entry(request, query)
            elif query in ent.lower():
                results.append(ent)
        if len(results) == 0:
            return render(request, "encyclopedia/error.html", {
                "error": "No results found"
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": results,
                "message": f"Search results for '{query}'"
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Invalid request"
        })

def new(request):
    if request.method =="POST":
        title = request.POST.get("title").capitalize()
        content = request.POST.get("content")
        wholeContent = f"# {title}\n\n{content}"
        
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "error": "Entry already exists"
            })
        else:
            util.save_entry(title, wholeContent)
            return entry(request, title)

    elif request.method == "GET":
        return render(request, "encyclopedia/newpage.html")

    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Invalid request"
        })

def edit(request, title):
    if request.method =="POST":
        content = request.POST.get("content")
        print(content)
        util.save_entry(title, content)
        return entry(request, title)
    elif request.method == "GET":
        content = util.get_entry(title)
        return render(request,  "encyclopedia/editpage.html", {
            "title": title,
            "content": content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Invalid request"
        })


    


