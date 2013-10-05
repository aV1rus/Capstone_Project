from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm
from .forms import UploadProjectForm

@login_required(login_url="login.views.connect")
def projects(request):
    return render_to_response('home/projects/projects.html', locals())


# @login_required(login_url="login.views.connect")
# def addNew(request):
#     return render_to_response('home/projects/addNew.html', {'first_name': request.user.first_name})


@login_required(login_url="login.views.connect")
def addNew(request):
    error = False
    message = ""
    if request.method == "POST" :
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            message = "valid"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # user = authenticate(username=username, password=password)
            # if user:
            #     login(request, user)
            #     return redirect("home.views.home")
            # else:
            #     error = True
            #     message = "Invalid credentials"

        else:
            message = "Fields incomplete."
            error = True
    else:
        form = CreateProjectForm()
    return render(request, "home/projects/addNew.html", locals())

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadProjectForm()
#     return render_to_response('upload.html', {'form': form})