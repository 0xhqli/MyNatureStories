from django.shortcuts import render, redirect
from SitSpots.models import *
from staffapp.models import *


def stories_main(request):
    posts = Post.objects.all()
    context ={
        "posts" : posts,
    }
    return render(request, "naturestories/stories_main.html", context)