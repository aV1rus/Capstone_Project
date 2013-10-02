# Create your views here.
from django.shortcuts import render, redirect
from settings.forms import SettingsFom
from django.contrib.auth.decorators import login_required

@login_required(login_url="login.views.connect")
def settings(request):
    form = SettingsFom(initial={'first_name': request.user.first_name})
    return render(request, "home/settings/settings.html", locals())