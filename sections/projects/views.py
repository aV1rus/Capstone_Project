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
    error = True
    message = ''
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            message = 'valid'
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            project = Projects(user=request.user, name=title, description=description)
            project.save()
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
        form = CreateProjectForm()

    return render(request, "home/projects/addNew.html", locals())


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