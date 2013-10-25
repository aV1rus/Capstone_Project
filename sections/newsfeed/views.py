from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import NewsFeed

@login_required(login_url="login.views.connect")
def newsfeed(request):
    #TODO :: filter newsfeed for only friends or projects user is invloved in
    newsfeed_list = NewsFeed.objects.all().order_by('-created_at')
    return render_to_response('home/newsfeed/newsfeed.html', locals())