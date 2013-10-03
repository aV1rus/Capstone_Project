# Create your views here.
from django.shortcuts import render, redirect
from settings.forms import SettingsFom
from django.contrib.auth.decorators import login_required

@login_required(login_url="login.views.connect")
def settings(request):
    if request.method == 'POST':
        form = SettingsFom(request.POST);
        if form.is_valid:
            form.save()
    else:
            form = SettingsFom(initial={'first_name' :request.user.first_name,'last_name' :request.user.last_name,
            'email': request.user.email})

    return render(request, "home/settings/settings.html", locals())