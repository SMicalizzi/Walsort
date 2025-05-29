from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from django import forms

from .forms import SimpleForm, Item


def index(request):
    return HttpResponse("Hello, world. You're at the forms index.")


def form(request):
    if request.method == "POST":
        f = SimpleForm(request.POST)
        if 'Add' in request.POST:
            data = request.POST
            item = data.get("iname")
            category = data.get("category")
            g = Item(item, category)
            catIndex = g.getCategoryIndex
            f.add_item(g)
            grocery_list = f.user_list
            categories = g.category_list
            newList = f.sort_list
            context = {"sorted_list": newList,"catIndex": catIndex}
            return render(request, "forms/form.html", context)
        else:
            newList = f.sort_list
            context = {"newList": newList}
            return render(request, "forms/form.html", context)
        """if f.is_valid():
            item = request.POST.get("iname")
            f.add_item(item)
            return HttpResponse(f) #render(request, "forms/form.html", {"form": form})
        else:
            return HttpResponse(f.is_valid())"""
    else:
        f = SimpleForm()
        return render(request, "forms/form.html", {"form": form})