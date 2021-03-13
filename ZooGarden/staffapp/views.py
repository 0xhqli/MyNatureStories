from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from staffapp.models import *
from SitSpots.models import *
from .forms import loginForm, tagForm, zoneForm
from .admin import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required



def root(request):
    return redirect('/accounts/login')

@login_required(login_url='/accounts/login')
@permission_required('staffapp.add_myuser',raise_exception=True) 
def register(request):
    print(request.POST)
    form = UserCreationForm()
    context = { 
        "form": form,
        "action": '/accounts/create',
        'button': 'Register'
    }
    return render(request, "staff/adminforms.html", context)

@login_required(login_url='/accounts/login')
@permission_required('staffapp.add_myuser',raise_exception=True) 
def regchk(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user=form.save()
        messages.success(request, 'Account created successfully')
        return redirect('/accounts')
    else:
        print(form.errors.items())
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect('/accounts/register')

@login_required(login_url='/accounts/login')
def adminpage(request):
    flaggedposts=list(Post.objects.filter(flagged=False))
    flaggedcomments=list(Comment.objects.filter(flagged=False))
    flaggedreplies=list(Reply.objects.filter(flagged=False))
    context={
        'pflaggedforreview': flaggedposts,
        'cflaggedforreview': flaggedcomments,
        'rflaggedforreview': flaggedreplies,
        'userslist': MyUser.objects.all(),
        'tags': Tag.objects.all(),
        'zones': Zone.objects.all(),
    }
    return render(request, "staff/adminpage.html", context)

def loginpage(request):
    print(request.POST)
    form = loginForm()
    context = { 
        "form": form,
        "action": '/accounts/logmein',
        'button': 'Login'
    }
    return render(request, "staff/adminforms.html", context)

def loginchk(request):
    form = loginForm(request.POST)
    form.is_valid()
    pw=form.cleaned_data.get("password")
    username=form.cleaned_data.get("username")
    user=authenticate(username=username,password=pw)
    if user:
        login(request, user)
        messages.success(request, 'Logged in successfully')
        return redirect('/accounts')
    else:
        messages.error(request, f"<div class='error'><ul><li>Invalid Credentials</li></ul></div>")
    return redirect('/accounts/login')

@login_required(login_url='/accounts/login')
@permission_required('SitSpots.add_tag',raise_exception=True) 
def tags(request):
    print(request.POST)
    form = tagForm()
    context = { 
        "form": form,
        "action": '/accounts/tags/create',
        'button': 'Add'
    }
    return render(request, "staff/adminforms.html", context)

@login_required(login_url='/accounts/login')
@permission_required('SitSpots.add_tag',raise_exception=True) 
def mktags(request):
    form = tagForm(request.POST)
    if form.is_valid():
        tag=form.save()
        messages.success(request, 'Tag created successfully')
        return redirect('/accounts')
    else:
        print(form.errors.items())
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect('/accounts/tags/new')

@login_required(login_url='/accounts/login')
@permission_required('SitSpots.add_zone',raise_exception=True) 
def zones(request):
    print(request.POST)
    form = zoneForm()
    context = { 
        "form": form,
        "action": '/accounts/zones/create',
        'button': 'Add'
    }
    return render(request, "staff/adminforms.html", context)

@login_required(login_url='/accounts/login')
@permission_required('SitSpots.add_zone',raise_exception=True) 
def mkzones(request):
    form = zoneForm(request.POST)
    if form.is_valid():
        zone=form.save()
        messages.success(request, 'Zone created successfully')
        return redirect('/accounts')
    else:
        print(form.errors.items())
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect('/accounts/zones/new')

@login_required(login_url='/accounts/login')
def logoutfun(request):
    logout(request)
    return redirect("/accounts/logout/success")

def logoutsuccess(request):
    return render(request, 'staff/loggedout.html')
    