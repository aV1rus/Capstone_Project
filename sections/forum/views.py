from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Major
from sections.newsfeed.models import NewsFeed
from .models import *
from .forms import *
import Constants


@login_required(login_url="login.views.connect")
def forum(request):
    # select m.name as name, m.acr as acr, COUNT(ft.id) as count, (select created_at from forum_comments where thread_ref_id=ft.id ORDER BY created_at DESC LIMIT 1 ) as last_post from home_major m JOIN forum_thread ft ON ft.category_id=m.id ORDER BY COUNT Desc;
    category_list = Major.objects.all()
    # category_list = Major.objects.raw("select m.name as name, m.acr as acr, COUNT(ft.id) as count, (select created_at from forum_comments where thread_ref_id=ft.id ORDER BY created_at DESC LIMIT 1 ) as last_post from home_major m JOIN forum_thread ft ON ft.category_id=m.id ORDER BY COUNT Desc")
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
                Comments(user=request.user, title=title, body=body, thread_ref=thread).save()
                PROJECT_URL = "/home/forum/threads/view?threadId="+str(thread.id)
                NewsFeed(user=request.user, title=Constants.NEWSFEED_FORUM_THREAD_NEW.format(request.user, category.name, title), url=PROJECT_URL).save()
                return redirect(PROJECT_URL)

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