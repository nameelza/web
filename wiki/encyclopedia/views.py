from re import S
from django.shortcuts import render

from . import util

import markdown2


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
    return render(request, "encyclopedia/newpage.html")


    


