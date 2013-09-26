# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="login.views.connect")
def settings(request):
    return render(request, "home/settings/settings.html", locals())