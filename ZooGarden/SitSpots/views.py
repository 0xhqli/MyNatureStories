from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from SitSpots.models import *
from staffapp.models import MyUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required



# def root(request):
#     return HttpResponse("sit spots")

def index(request):
    
    return render(request, "sitspots/index.html")

def zooGarden(request):
    context={
        'sub':"sitspots/californiaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def californiaGarden(request):
    context={
        'sub':"sitspots/californiaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def southAmericaGarden(request):
    context={
        'sub':"sitspots/southAmericaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def northAmericaGarden(request):
    context={
        'sub':"sitspots/northAmericaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def australiaGarden(request):
    context={
        'sub':"sitspots/australiaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def africaGarden(request):
    context={
        'sub':"sitspots/africaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def bajaCaliforniaGarden(request):
    context={
        'sub':"sitspots/bajaCaliforniaGarden.html"
    }
    return render(request, "sitspots/zooGarden.html",context)

def zGardenAjax(request):
    print(request.POST)
    return render(request, f"sitspots/{request.POST['zone']}",)

def findYourSitSpot(request):
    context={
        'route':"Find your sitspot"
    }
    return render(request, "sitspots/sitspots.html",context)
def about(request):
    context={
        'route':"about"
    }
    return render(request, "sitspots/about.html",context)
def contact(request):
    context={
        'route':"contact"
    }
    return render(request, "sitspots/contact.html",context)







# def groupcreate()