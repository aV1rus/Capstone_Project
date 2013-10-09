from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

@login_required(login_url="login.views.connect")
def userProfile(request):
    if request.method == 'GET':
        if request.GET:
            #TODO :: link to Profile instead of user
            user_id = request.GET['userId']
            user = User.objects.get(id=user_id)
            user_profile = Profile.objects.get(user=user)
    return render_to_response('home/user_profile/profile.html', locals())