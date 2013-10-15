import Constants
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from sections.projects.models import *
from sections.newsfeed.models import NewsFeed

@login_required(login_url="login.views.connect")
def projects(request):
    project_list = Projects.objects.all()
    return render(request, 'home/projects/projects.html', locals())


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
                #TODO :: HANDLE UPLOAD OF FILE
                project.save()
                project_id = project.id
                #Add to newsfeed
                Project_URL = "/home/projects/project_info?projId="+str(project_id)
                NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_CREATE.format(request.user, title), url=Project_URL).save()
                return redirect(Project_URL)

                # if project:
                #     uploadFile(request.FILES['file'], 'Initial Upload')
                #     message = 'Completed'
                # else:
                #     error = True
                #     message = 'OOPS. Error'

        else:
            message = 'Fields incomplete.'
            error = True
    else:
        form = CreateProjectForm()

    return render(request, "home/projects/addNew.html", locals())


@login_required(login_url="login.views.connect")
def projectInfo(request):
    if request.method == 'GET':
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)
            project_files = ProjectFile.objects.filter(project_ref=project_id)
        else:
            project_list = Projects.objects.all()
    return render(request, 'home/projects/project_info.html', locals())


@login_required(login_url="login.views.connect")
def addFile(request):
    error = False
    if request.method == 'GET':
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)

    if request.method == "POST":
        form = AddFileForm(request.POST)
        if form.is_valid():
            project_id = request.POST['projId']
            project = Projects.objects.get(id=project_id)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            file = ProjectFile(project_ref=project, user=request.user, name=name, description=description)
            if file:
                #TODO :: HANDLE UPLOAD OF FILE
                file.save()
                FileUpdates(file_ref=file, user=request.user, description='Initial Upload', file_location='TEST').save()
                # handle_uploaded_file(request.FILES['file'])
                PROJECT_URL = "/home/projects/project_info?projId="+project_id
                NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_COMMIT.format(request.user, project.name), url=PROJECT_URL).save()
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
        form = UploadFileForm(request.POST)
        if form.is_valid():
            file_id = request.POST['fileId']
            file = ProjectFile.objects.get(id=file_id)
            description = form.cleaned_data['description']
            file_update = FileUpdates(file_ref=file, user=request.user, description=description, file_location='TEST')
            if file_update:
                #TODO :: HANDLE UPLOAD OF FILE
                file_update.save()
                # handle_uploaded_file(request.FILES['file'])
                PROJECT_URL = "/home/projects/file_info?fileId="+file_id
                # NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_COMMIT.format(request.user, project.name), url=PROJECT_URL).save()
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


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
