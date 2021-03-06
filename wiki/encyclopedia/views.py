from re import S
from django.shortcuts import render

from . import util

import markdown2
import secrets

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
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

def search(request):
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

def random(request):
    entries = util.list_entries()
    return entry(request, secrets.choice(entries))
    


