from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from sections.projects.models import *
from sections.forum.models import *

@login_required(login_url="login.views.connect")
def userProfile(request):
    if request.method == 'GET':
        if request.GET:
            #TODO :: link to Profile instead of user
            user_id = request.GET['userId']
            user = User.objects.get(id=user_id)
            user_profile = Profile.objects.get(user=user)
            projects = Projects.objects.filter(user=user)

            #organize the threads
            threads = Thread.objects.filter(user=user)
            for t in threads:
                comments = Comments.objects.filter(thread_ref=t).order_by('created_at')
                if comments:
                    t.title = comments[0].title
                    t.count = comments.count()
                    t.last_post = comments[comments.count()-1]

    return render(request, 'home/user_profile/profile.html', locals())