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

def storiesck(request):
    print(request.POST)
    form = PostForm(request.POST, request.FILES) 
    if form.is_valid():
        author = form.cleaned_data.get("author")
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        sitspot = form.cleaned_data.get("sitspot")
        website = form.cleaned_data.get("website")
        image = form.cleaned_data.get("image")
        zone = form.cleaned_data.get("zone")
        user = form.cleaned_data.get("user")
        new_post = Post.objects.create(author=author, user=user, title=title, content=content, website=website, image=image, zone=zone, sitspot=sitspot)
        new_post.save()
        return redirect("/naturestories")
    else:
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect('/naturestories/create')

def stories_read_more(request, numb):
    this_post = Post.objects.get(id=numb)
    form = CommentForm(request.POST)
    context ={
        "post" : this_post,
        "comment_form" : form,
    }
    print("*"*40)
    print(this_post.image.url)
    return render(request, "naturestories/stories_read_more.html", context)
    
def new_comment(request):
    print(request.POST)
    form = CommentForm(request.POST)
    if form.is_valid():
        author = form.cleaned_data.get("author")
        content = form.cleaned_data.get("content")
        post = Post.objects.get(id = request.POST["post_id"])
        new_comment = Comment.objects.create(author=author, content=content, post=post)
        new_comment.save()
        return redirect(f'/naturestories/{request.POST["post_id"]}')    
    else:
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect(f'/naturestories/{request.POST["post_id"]}')

