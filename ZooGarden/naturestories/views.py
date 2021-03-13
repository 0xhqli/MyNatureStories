from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from SitSpots.models import *
from staffapp.models import *
from .forms import *
import random, math 
from PIL import Image

def stories_main(request):
    posts = Post.objects.all().order_by("-created_at")
    context ={
        "posts" : posts,
        "Zones": Zone.objects.all()
    }
    return render(request, "naturestories/stories_main.html", context)

def stories_partial(request):
    print(request.POST)
    if request.POST['zone']=='all':
        posts = Post.objects.all().order_by("-created_at")
    else:
        posts=Post.objects.filter(zone__name=request.POST['zone']).order_by("-created_at")
    context ={
        "posts" : posts,
    }
    return render(request, "naturestories/stories_list.html", context)

def stories_search_partial(request):
    print(request.POST)
    posts_search_by_title=Post.objects.filter(title__contains=request.POST['search']).order_by("-created_at")
    posts_search_by_content=Post.objects.filter(content__contains=request.POST['search']).order_by("-created_at")
    context ={
        "posts" : posts_search_by_title|posts_search_by_content,
    }
    return render(request, "naturestories/stories_list.html", context)

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
        if 'add_a_location' in request.POST:
            lat=form.cleaned_data.get("lat")
            lng=form.cleaned_data.get("lng")
            new_post = Post.objects.create(author=author, user=user, title=title, content=content, website=website, image=image, zone=zone, sitspot=sitspot,lat=lat,lng=lng)
        else:
            new_post = Post.objects.create(author=author, user=user, title=title, content=content, website=website, image=image, zone=zone, sitspot=sitspot)
        new_post.save()
        print(new_post.image.url)
        #exif strip begin
        uu=new_post.image.url[1:]
        print(uu)
        image= Image.open(new_post.image)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save(uu)
        #exif strip end
        return redirect("/naturestories")
    else:
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect('/naturestories/create')

def stories_read_more(request, numb):
    this_post = Post.objects.get(id=numb)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    context ={
        "post" : this_post,
        "comment_form" : comment_form,
        "reply_form" : reply_form,
    }
    print("*"*40)
    print(this_post.image.url)
    # uu=this_post.image.url[1:]
    # print(uu)
    # image= Image.open(this_post.image)
    # data = list(image.getdata())
    # image_without_exif = Image.new(image.mode, image.size)
    # image_without_exif.putdata(data)
    # image_without_exif.save(uu)
    return render(request, "naturestories/stories_read_more.html", context)
    
def new_comment(request):
    print(request.POST)
    form = CommentForm(request.POST)
    if form.is_valid():
        author = form.cleaned_data.get("author")
        content = form.cleaned_data.get("content")
        post = Post.objects.get(id = request.POST["post_id"])
        icon = math.floor(random.random()*5)+1
        new_comment = Comment.objects.create(author=author, content=content, post=post, icon=icon)
        new_comment.save()
        return redirect(f'/naturestories/{request.POST["post_id"]}')    
    else:
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect(f'/naturestories/{request.POST["post_id"]}')

def new_reply(request):
    print("*"*40)
    print(request.POST)
    form = ReplyForm(request.POST)
    # hidden input: "comment_id", "post_id"
    if form.is_valid():
        author = form.cleaned_data.get("author")
        content = form.cleaned_data.get("content")
        comment = Comment.objects.get(id = request.POST["comment_id"])
        new_reply = Reply.objects.create(author=author, content=content, comment=comment)
        new_reply.save()
        return redirect(f'/naturestories/{request.POST["post_id"]}')
    else:
        for x, y in form.errors.items():
            messages.error(request, f"<div class='error'>{x.capitalize().replace('_',' ')}{y}</div>")
        return redirect(f'/naturestories/{request.POST["post_id"]}')

def new_reply_ajax(request):
    print("*"*40)
    print(request.POST)
    form = ReplyForm(request.POST)
    # hidden input: "comment_id", "post_id"
    if form.is_valid():
        author = form.cleaned_data.get("author")
        content = form.cleaned_data.get("content")
        comment = Comment.objects.get(id = request.POST["comment_id"])
        new_reply = Reply.objects.create(author=author, content=content, comment=comment)
        new_reply.save()
        this_post=comment.post
        reply_form = ReplyForm()
        context ={
            "post" : this_post,
            "reply_form" : reply_form,
        }
        print("*"*40)
        return render(request, "naturestories/stories_comments_and_replies.html", context)
    else:
        err={}
        for x, y in form.errors.items():
            err[x]=y.__str__
        return JsonResponse(err)

def new_comment_ajax(request):
    print("*"*40)
    print(request.POST)
    form = CommentForm(request.POST)
    if form.is_valid():
        author = form.cleaned_data.get("author")
        content = form.cleaned_data.get("content")
        post = Post.objects.get(id = request.POST["post_id"])
        icon = math.floor(random.random()*5)+1
        new_comment = Comment.objects.create(author=author, content=content, post=post, icon=icon)
        new_comment.save()
        reply_form = ReplyForm()
        context ={
            "post" : post,
            "reply_form" : reply_form,
        }
        print("*"*40)
        return render(request, "naturestories/stories_comments_and_replies.html", context)
    else:
        err={}
        for x, y in form.errors.items():
            err[x]=y.__str__
        return JsonResponse(err)
