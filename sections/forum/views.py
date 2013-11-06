from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Major
from sections.newsfeed.models import NewsFeed
from sections.projects.models import ProjectMembers
from .models import *
from .forms import *
import Constants


@login_required(login_url="login.views.connect")
def forum(request):
    category_list = Major.objects.all().order_by('name')

    for c in category_list:
        category = Major.objects.get(name=c.name)
        threads = Thread.objects.filter(category=category)
        c.count = threads.count()
        ct = 0
        comments = Comments.objects.filter(thread_ref__in=threads).order_by('-created_at')
        if comments:
            c.last_post = comments[0].created_at

    # category_list = sorted(category_list, key=operator.attrgetter('last_post'))

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
            for t in thread_list:
                comments = Comments.objects.filter(thread_ref=t).order_by('created_at')
                if comments:
                    t.title = comments[0].title
                    t.count = comments.count()
                    t.last_post = comments[comments.count()-1]

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
                PROJECT_URL = Constants.ROOT_URL(request.path)+"/home/forum/threads/view?threadId="+str(thread.id) #"sections.forum.views.thread_view?threadId="+str(thread.id)
                NewsFeed(user=request.user, title=Constants.NEWSFEED_FORUM_THREAD_NEW.format(request.user, category.name, title), url=PROJECT_URL).save()
                return redirect(PROJECT_URL)

        else:
            message = 'Fields incomplete.'
            error = True
    else:
        form = CreateThreadForm()

    return render(request, "home/forum/threads_new.html", locals())

@login_required(login_url="login.views.connect")
def editComment(request):
    if request.method == 'GET':
        if request.GET:
            comment_id = request.GET['commentid']
            # cnt = request.GET['cnt']
            comment = Comments.objects.get(id=comment_id)
            form = CreateThreadForm(initial={'title': comment.title, 'body': comment.body})

    if request.method == "POST":
        form = CreateThreadForm(request.POST)
        if form.is_valid():
            comment_id = request.POST['commentid']
            comment = Comments.objects.get(id=comment_id)
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            if title != '':
                comment.title = title
            if body != '':
                comment.body = body
            comment.save()
            thread_id = comment.thread_ref_id
            PROJECT_URL = Constants.ROOT_URL(request.path)+"/home/forum/threads/view?threadId="+str(thread_id) #"sections.forum.views.thread_view?threadId="+str(thread.id)
            return redirect(PROJECT_URL)
        else:
            message = 'Fields incomplete.'
            error = True

    return render(request, 'home/forum/threads_new.html', locals())

@login_required(login_url="login.views.connect")
def linkProject(request):
    if request.method == 'GET':
        if request.GET:
            thread_id = request.GET['threadId']
            thread = Thread.objects.get(id=thread_id)

            if 'proj_ref' in request.GET:
                project = Projects.objects.get(id=request.GET['proj_ref'])
                if ProjectForum.objects.filter(project=project, thread=thread):
                    Error = True
                    message = 'That Project is already part of this Thread'
                else:
                    ProjectForum(project=project, thread=thread).save()

            if 'del_proj_ref' in request.GET:
                project = Projects.objects.get(id=request.GET['del_proj_ref'])
                ProjectForum.objects.get(project=project, thread=thread).delete()

        linked_projects = ProjectForum.objects.filter(thread=thread)
        project_list = Projects.objects.filter(user=request.user)
        project_member_list = ProjectMembers.objects.filter(user=request.user)

    return render(request, 'home/forum/link_project.html', locals())


@login_required(login_url="login.views.connect")
def thread_view(request):
    if request.method == 'GET':
        if request.GET:
            thread_id = request.GET['threadId']
            thread = Thread.objects.get(id=thread_id)

    if request.method == "POST":
        form = CreateThreadForm(request.POST)
        if form.is_valid():
            thread_id = request.POST['catId']
            thread = Thread.objects.get(id=thread_id)
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            Comments(user=request.user, title=title, body=body, thread_ref=thread).save()
    else:
        form = CreateThreadForm()

    linked_projects = ProjectForum.objects.filter(thread=thread)
    comment_list = Comments.objects.filter(thread_ref=thread)
    for c in comment_list:
        c.body = c.body.replace('[IMG]', Constants.IMAGE_URL_BEGIN).replace('[/IMG]', Constants.IMAGE_URL_END)
        c.body = c.body.replace('[U2]', Constants.VIDEO_URL_BEGIN).replace('[/U2]', Constants.VIDEO_URL_END)

    return render(request, 'home/forum/threads_view.html', locals())
