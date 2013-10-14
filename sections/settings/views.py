# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from sections.user_profile.models import Profile

from sections.settings.forms import SettingsForm


@login_required(login_url="login.views.connect")
def settings(request):
    #Retrieve associated user user_profile
    profile = Profile.objects.get(user = request.user)
    notify = False
    message = ""
    if request.method == 'POST':
        form = SettingsForm(request.POST);
        if form.is_valid():
            m_user = User.objects.get(id = request.user.id)
            m_user.first_name = form.cleaned_data['first_name']
            m_user.last_name = form.cleaned_data['last_name']
            m_user.email = form.cleaned_data['email']
            m_user.save()
            profile.major = form.cleaned_data['major']
            profile.headline = form.cleaned_data['headline']
            profile.save();
            notify = True
            message = "Information correctly updated."

        else:
            notify = True
            message = "Form is not valid."



    else:
        form = SettingsForm(initial={'first_name' :request.user.first_name,'last_name' :request.user.last_name,
            'email': request.user.email, 'major': profile.major, 'headline': profile.headline})

    return render(request, "home/settings/settings.html", locals())