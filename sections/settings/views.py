# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from login.models import Profile

from sections.settings.forms import SettingsFom


@login_required(login_url="login.views.connect")
def settings(request):
    if request.method == 'POST':
        form = SettingsFom(request.POST);
        if form.is_valid:
            m_user = User.objects.get(id = request.user.id)
            #m_user.email = "lolo@spsu.edu"
            #m_user.save()


    else:
        form = SettingsFom(initial={'first_name' :request.user.first_name,'last_name' :request.user.last_name,
            'email': request.user.email})

    return render(request, "home/settings/settings.html", locals())