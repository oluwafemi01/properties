from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import properties
from .forms import propertiesForm
from .filters import propertiesFilter
import requests
import json
# Create your views here.

@login_required
def add(request):
    mess = ""
    if request.method == "POST" :
        mess = "Invalid Input"
        form = propertiesForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            mess = "created successfully"
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
        else:
            mess = "Error creating properties"
    return render(request,"properties/add.html",{"title":"Add Properties","message":mess})


def search(request):
    user_filter = ""
    if len(request.GET) > 0:
        properties_list = properties.objects.all()
        user_filter = propertiesFilter(request.GET, queryset=properties_list)
    return render (request, 'properties/search.html',{"title":"search properties","properties":user_filter})

def all(request):

    #headers={"content-type":"application/json"}
    #url ="http://127.0.0.1:8000/api/all"
    #r = requests.get(url, headers=headers)
    #show_post = json.loads(r.text)

    #print(r)
    #for g in show_post:
    #    print(g["title"])
    #    print(g["location"])
    show_post = properties.objects.all()
    #print(r.text)
    return render(request,"properties/list_all.html",{"title":"All properties","properties":show_post})

def details(request,pk):
    show_post = properties.objects.get(id=pk)
    return render(request,"properties/details.html",{"title":"show properties","property":show_post})
