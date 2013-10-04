# Create your views here.
from django.http import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

@login_required(login_url="login.views.connect")
def home(request):
    return HttpResponseRedirect("/home/forum")

    # return render(request, 'home/home.html', locals())
