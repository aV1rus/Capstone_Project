from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url="login.views.connect")
def projects(request):
    return render_to_response('home/projects/projects.html', locals())