import Constants
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm, UploadProjectForm
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
                ProjectUpdates(project_ref=project, user=request.user, description='Initial Upload', file_location='TEST').save()
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
            project_updates = ProjectUpdates.objects.filter(project_ref=project_id)
        else:
            project_list = Projects.objects.all()
    return render(request, 'home/projects/project_info.html', locals())


@login_required(login_url="login.views.connect")
def commit(request):
    error = False
    if request.method == 'GET':
        if request.GET:
            project_id = request.GET['projId']
            project = Projects.objects.get(id=project_id)

    if request.method == "POST":
        form = UploadProjectForm(request.POST)
        if form.is_valid():
            project_id = request.POST['projId']
            project = Projects.objects.get(id=project_id)
            description = form.cleaned_data['description']
            update = ProjectUpdates(project_ref=project, user=request.user, description=description, file_location='TEST')
            if update:
                #TODO :: HANDLE UPLOAD OF FILE
                update.save()
                # handle_uploaded_file(request.FILES['file'])
                PROJECT_URL = "/home/projects/project_info?projId="+project_id
                NewsFeed(user=request.user, title=Constants.NEWSFEED_PROJECT_COMMIT.format(request.user, project.name), url=PROJECT_URL).save()
                return redirect(PROJECT_URL)
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
        form = UploadProjectForm()

    return render(request, 'home/projects/commit.html', locals())


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
