from django.shortcuts import render, redirect
from SitSpots.models import *
from staffapp.models import *
from .forms import *


def stories_main(request):
    posts = Post.objects.all()
    context ={
        "posts" : posts,
    }
    return render(request, "naturestories/stories_main.html", context)

def stories_create(request):
    form = PostForm()
    context ={
        "form" : form,
    }
    return render(request, "naturestories/stories_create.html", context)

def stories_read_more(request, numb):
    this_post = Post.objects.get(id=numb)
    context ={
        "post" : this_post,
    }
    return render(request, "naturestories/stories_read_more.html", context)
    