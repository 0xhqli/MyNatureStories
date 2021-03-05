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
    
    return render(request, "sitspots/zooGarden.html",)

def californiaGarden(request):

    return render(request, "sitspots/californiaGarden.html",)

def southAmericaGarden(request):
    
    return render(request, "sitspots/southAmericaGarden.html",)

def northAmericaGarden(request):
    
    return render(request, "sitspots/northAmericaGarden.html",)

def australiaGarden(request):
    
    return render(request, "sitspots/austaliaGarden.html",)

def africaGarden(request):
    
    return render(request, "sitspots/africaGarden.html",)

def bajaCaliforniaGarden(request):
    
    return render(request, "sitspots/bajaCaliforniaGarden.html",)







# def groupcreate()