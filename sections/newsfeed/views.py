from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url="login.views.connect")
def newsfeed(request):
    return render_to_response('home/newsfeed/newsfeed.html', {'first_name': request.user.first_name})