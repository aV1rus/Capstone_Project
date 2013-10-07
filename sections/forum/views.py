from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Major
from .models import *


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
            category_id = request.GET['category_id']
            category = Major.objects.get(id=category_id)
            thread_list = Thread.objects.filter(category=category)

    return render(request, 'home/forum/threads.html', locals())

@login_required(login_url="login.views.connect")
def thread_new(request):
    return render(request, 'home/forum/threads_new.html', locals())