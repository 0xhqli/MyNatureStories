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

    return render(request, "sitspots/zooGarden.html")

# def groupcreate()