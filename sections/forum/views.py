from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Major
from .models import *
from forms import *


@login_required(login_url="login.views.connect")
def forum(request):
    category_list = Major.objects.all()
    return render(request, 'home/forum/forum.html', locals())


@login_required(login_url="login.views.connect")
def findUsers(request):
    searchFilter = ''
    if request.method == 'GET':
        if request.GET:
            searchFilter = request.GET['searchFilter']
            users = User.objects.filter(username__contains=searchFilter) | User.objects.filter(email__contains=searchFilter) | User.objects.filter(first_name__contains=searchFilter)
        else:
            users = User.objects.all()
    else:
        users = User.objects.all()

    return render(request, 'home/forum/users.html', locals())


@login_required(login_url="login.views.connect")
def threads(request):
    if request.method == 'GET':
        if request.GET:
            category_id = request.GET['catId']
            category = Major.objects.get(id=category_id)
            thread_list = Thread.objects.filter(category=category)

    return render(request, 'home/forum/threads.html', locals())

@login_required(login_url="login.views.connect")
def thread_new(request):
    error = False
    message = ''
    if request.method == 'GET':
        if request.GET:
            category_id = request.GET['catId']

    if request.method == "POST":
        form = CreateThreadForm(request.POST)
        if form.is_valid():
            category_id = request.POST['catId']
            category = Major.objects.get(id=category_id)
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            thread = Thread(user=request.user, category=category)
            if thread:
                thread.save()
                comment = Comments(user=request.user, title=title, body=body, thread_ref=thread)
                comment.save()
                return redirect("/home/forum/threads/view?threadId="+str(thread.id))

        else:
            message = 'Fields incomplete.'
            error = True
    else:
        form = CreateThreadForm()

    return render(request, "home/forum/threads_new.html", locals())


@login_required(login_url="login.views.connect")
def thread_view(request):
    if request.method == 'GET':
        if request.GET:
            thread_id = request.GET['threadId']

    thread = Thread.objects.get(id=thread_id)
    comment_list = Comments.objects.filter(thread_ref=thread)
    return render(request, 'home/forum/threads_view.html', locals())