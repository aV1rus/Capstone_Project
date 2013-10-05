from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from models import *
from .forms import CreateProjectForm
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import UploadProjectForm

@login_required(login_url="login.views.connect")
def projects(request):
    project_list = Projects.objects.all()
    return render_to_response('home/projects/projects.html', locals())


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
            project.save()
            message = 'valid'
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
    return render_to_response('home/projects/project_info.html', locals())


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
            update.save()
            error = True
            message = 'yay'
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


    # def upload_file(request):
    #     if request.method == 'POST':
    #         form = UploadProjectForm(request.POST, request.FILES)
    #         # if form.is_valid():
    #         #     handle_uploaded_file(request.FILES['file'])
    #         #     return HttpResponseRedirect('/success/url/')
    #     else:
    #         form = UploadProjectForm()
    #     return render_to_response('upload.html', {'form': form})


    # def uploadFile(file, description):
    #     return