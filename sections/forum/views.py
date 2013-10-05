from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from login.models import Profile

@login_required(login_url="login.views.connect")
def forum(request):
    return render_to_response('home/forum/forum.html', locals())


@login_required(login_url="login.views.connect")
def findUsers(request):
    users = Profile.objects.all()
    return render_to_response('home/forum/users.html', locals())