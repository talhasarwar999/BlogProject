from django.shortcuts import render, HttpResponse, redirect
from blog.forms import *
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def blogs(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/blogs.html",context)


def blogss(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    post_like = Post.objects.get(slug=slug)
    total_likes = post_like.likes.count()
    ta=post_like.likes.filter(id=request.user.id).exists()
    print(ta)
     # comment = comments.user.username
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict,'like':total_likes,'ta':ta}
    return render(request, "blog/blogss.html", context)
def blogsss(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    post_like = Post.objects.get(slug=slug)
    print(post_like)
    ta = post_like.likes.filter(id=request.user.id).exists()
    print(ta)
    if post_like.likes.filter(id=request.user.id).exists():
        post_like.likes.remove(request.user)
    else:
        post_like.likes.add(request.user)
        post_like.save()
    total_likes = post_like.likes.count()
    # comment = comments.user.username
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict,'like':total_likes,'ta':ta}
    return render(request, "blog/blogss.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        # reply=request.POST.get('reply')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')

        if parentSno=="":
         if len(comment) <= 0:
           messages.error(request, "Please enter valid comment")
         else:
           comment=BlogComment(comment= comment, user=user, post=post)
           comment.save()
           messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")
def delete(request,sno):
    movie = get_object_or_404(BlogComment, sno=sno)
    creator = movie.user.username
    if request.method=="POST" and request.user.username==creator:
     employee=BlogComment.objects.get(sno=sno)
     employee.delete()
     messages.success(request, "your comment has been deleted")

     return redirect('blogs')
    else:
        messages.error(request,"You are not allowed to delete the comment")
    return redirect('blogs')

def deletep(request, sno):
    allow = get_object_or_404(BlogComment, sno=sno)
    creatorr = allow.user.username
    if request.method == "POST" and request.user.username==creatorr:
        employee = BlogComment.objects.get(sno=sno)
        employee.delete()
        messages.success(request, "your reply has been deleted")

        return redirect('blogs')
    else:
        messages.error(request, "You are not allowed to delete the comment")
    return redirect('blogs')

def edit(request, sno):
    comment = BlogComment.objects.get(sno=sno)
    return render(request,'blog/editcom.html', {'comment':comment})
def update(request,sno):
    allow = get_object_or_404(BlogComment, sno=sno)
    creatorr = allow.user.username
    if request.method == "POST" and request.user.username == creatorr:
      comment = BlogComment.objects.get(sno=sno)
      print(comment)
      form = EmployeeForm(request.POST, instance= comment)
      if form.is_valid():
       form.save()
       messages.success(request, "Successfully Edit")
       return redirect('blogs')
    else:
      messages.error(request, "Not Eligible ")
      return redirect('blogs')
def editreply(request, sno):
    reply = BlogComment.objects.get(sno=sno)
    return render(request,'blog/editrep.html', {'reply':reply})
def updatereply(request,sno):
    allow = get_object_or_404(BlogComment, sno=sno)
    creatorr1 = allow.user.username
    if request.method == "POST" and request.user.username == creatorr1:
     reply = BlogComment.objects.get(sno=sno)
     form1 = EmployeeForm1(request.POST, instance= reply)
     if form1.is_valid():
      form1.save()
      messages.success(request, "Successfully Edit")
      return redirect('blogs')
     else:
       messages.error(request, "Not Edit")
    else:
      messages.error(request, "Not Eligible ")
    return redirect('blogs')
def BlogPostLike(request, sno):
    post_like=Post.objects.get(sno=sno)
    post_like.likes.add(request.user)
    post_like.save()
    total_likes=post_like.likes.count()
    return render(request,"blog/blogss.html",{'like':total_likes})