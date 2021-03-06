import Constants
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from sections.projects.models import *
from sections.forum.models import ProjectForum, Comments
from sections.newsfeed.models import NewsFeed

@login_required(login_url="login.views.connect")
def projects(request):
    contrib_projects = ProjectMembers.objects.filter(user=request.user)
    owned_project_list = Projects.objects.filter(user=request.user)
    return render(request, 'home/projects/projects.html', locals())


@login_required(login_url="login.views.connect")
def allProjects(request):
    project_list = Projects.objects.all()

    if request.method == 'GET':
        if request.GET:
            searchFilter = request.GET['searchFilter']
            project_list = Projects.objects.filter(name__icontains=searchFilter)

    return render(request, 'home/projects/all_projects.html', locals())


@login_required(login_url="login.views.connect")
def addNew(request):
    error = False
    message = ''
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            project = Projects(user=request.user, name=title, description=description)
            if project:
                project.save()
                project_id = project.id
                #Add to newsfeed
                Project_URL = Constants.ROOT_URL(request.path)+"/home/projects/project_info?projId="+str(project_id)
                PROJECT_VIEW = 'sections.projects.views.projectInfo'
                PROJECT_PARAMS = "?projId="+str(project_id)
                NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_CREATE.format(request.user, title), view=PROJECT_VIEW, params=PROJECT_PARAMS).save()
                return redirect(Project_URL)

        else:
            message = 'Fields incomplete.'
            error = True
    else:
        form = CreateProjectForm()

    return render(request, "home/projects/addNew.html", locals())

@login_required(login_url="login.views.connect")
def editProject(request):
    # form = CreateProjectForm()
    error = False
    message = ''
    if request.method == "GET":
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)
            form = CreateProjectForm(initial={'title': project.name, 'description': project.description})

    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)
            project.name = title
            project.description = description
            project.save()
            #Add to newsfeed
            Project_URL = Constants.ROOT_URL(request.path)+"/home/projects/project_info?projId="+str(project_id)
            PROJECT_VIEW = 'sections.projects.views.projectInfo'
            PROJECT_PARAMS = "?projId="+str(project_id)
            NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_EDIT.format(request.user, title), view=PROJECT_VIEW, params=PROJECT_PARAMS).save()
            return redirect(Project_URL)
        else:
            message = 'Fields incomplete.'
            error = True

    return render(request, "home/projects/addNew.html", locals())

@login_required(login_url="login.views.connect")
def projectInfo(request):
    if request.method == 'GET':
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)
            project_files = ProjectFile.objects.filter(project_ref=project_id)
            user_list = ProjectMembers.objects.filter(project=project)

            if request.user == project.user:
                is_owner = True
                is_member = True

            if user_list.count() > 0:
                for u in user_list:
                    if request.user == u.user:
                        is_member = True

            for p in project_files:
                files = FileUpdates.objects.filter(file_ref=p).order_by('-created_at')
                if files:
                    p.newest_file = files[0]
                    p.file_count = files.count()

            linked_projects = ProjectForum.objects.filter(project=project)

            for lp in linked_projects:
                comment_list = Comments.objects.filter(thread_ref=lp.thread).order_by("created_at")[:1]
                lp.thread.title = comment_list[0].title

    return render(request, 'home/projects/project_info.html', locals())


@login_required(login_url="login.views.connect")
def addFile(request):
    error = False
    if request.method == 'GET':
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)

    if request.method == "POST":
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            project_id = request.POST['projId']
            project = Projects.objects.get(id=project_id)
            name = form.cleaned_data['name']
            fileUpload = request.FILES["file"]
            description = form.cleaned_data['description']
            file = ProjectFile(project_ref=project, user=request.user, name=name, description=description)
            if file:
                #TODO :: HANDLE UPLOAD OF FILE
                file.save()
                FileUpdates(file_ref=file, user=request.user, description='Initial Upload', file_upload=fileUpload).save()
                # handle_uploaded_file(request.FILES['file'])
                PROJECT_URL = Constants.ROOT_URL(request.path)+"/home/projects/project_info?projId="+project_id
                PROJECT_VIEW = 'sections.projects.views.projectInfo'
                PROJECT_PARAMS = "?projId="+project_id
                NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_NEWFILE.format(request.user, project.name, file.name), view=PROJECT_VIEW, params=PROJECT_PARAMS).save()
                return redirect(PROJECT_URL)

        else:
            message = 'Fields incomplete.'
            error = True
    else:
        form = AddFileForm()

    return render(request, 'home/projects/addFile.html', locals())


@login_required(login_url="login.views.connect")
def fileUpdate(request):
    error = False
    if request.method == 'GET':
        if request.GET:
            file_id = request.GET['fileId']
            file = ProjectFile.objects.get(id=file_id)

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_id = request.POST['fileId']
            file = ProjectFile.objects.get(id=file_id)
            description = form.cleaned_data['description']
            fileUpload = request.FILES["file"]
            file_update = FileUpdates(file_ref=file, user=request.user, description=description, file_upload=fileUpload)
            if file_update:
                #TODO :: HANDLE UPLOAD OF FILE
                file_update.save()
                PROJECT_URL = Constants.ROOT_URL(request.path)+"/home/projects/file_info?fileId="+file_id
                PROJECT_VIEW = 'sections.projects.views.fileInfo'
                PROJECT_PARAMS = "?fileId="+file_id
                NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_COMMIT.format(request.user, file.project_ref.name), view=PROJECT_VIEW, params=PROJECT_PARAMS).save()
                return redirect(PROJECT_URL)

        else:
            message = 'Fields incomplete.'
            error = True
    else:
        form = UploadFileForm()

    return render(request, 'home/projects/project_info/update.html', locals())


@login_required(login_url="login.views.connect")
def fileInfo(request):
    error = False
    if request.method == 'GET':
        if request.GET:
            file_id = request.GET['fileId']
            file = ProjectFile.objects.get(id=file_id)
            file_uploads = FileUpdates.objects.filter(file_ref=file).order_by('-created_at')

    return render(request, 'home/projects/project_info/file_info.html', locals())


@login_required(login_url="login.views.connect")
def invite(request):
    searchFilter = ''
    users = User.objects.all()
    message = ''
    if request.method == 'GET':
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)
            searchFilter = request.GET['searchFilter']
            user_id = request.GET['userId']

            if searchFilter != "":
                users = User.objects.filter(username__icontains=searchFilter) | User.objects.filter(email__icontains=searchFilter) | User.objects.filter(first_name__icontains=searchFilter)

            if user_id != "":
                user = User.objects.get(id=user_id)
                if user != project.user:
                    check = ProjectMembers.objects.filter(user=user, project=project)
                    if check.count() is 0:
                        ProjectMembers(user=user, project=project).save()
                        PROJECT_URL = Constants.ROOT_URL(request.path)+'/home/user_profile/?userId='+str(user.id)
                        PROJECT_VIEW = 'sections.user_profile.views.userProfile'
                        PROJECT_PARAMS = "?userId="+str(user.id)
                        NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_INVITED.format(user, project.name), view=PROJECT_VIEW, params=PROJECT_PARAMS).save()
                        message = user.username+' added'
                    else:
                        message = user.username+' is already a memeber of '+project.name
                else:
                    message = user.username+' is the owner of '+project.name+"! Ofcourse he is a member"

    for u in users:
        u.proj_created = Projects.objects.filter(user=u).count()
        u.contributions = FileUpdates.objects.filter(user=u).count()

    return render(request, 'home/projects/invite.html', locals())


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
