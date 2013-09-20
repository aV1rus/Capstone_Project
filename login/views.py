from django.shortcuts import render,redirect
from login.forms import ConnectionForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


def disconnect(request):
    logout(request)
    return redirect(reverse("login.views.connect"))

def connect(request):
    error = False
    message = ""
    if request.method == "POST" :
        form = ConnectionForm(request.POST)
        if form.is_valid():
            message = "valid"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("home.views.home")
            else:
                error = True
                message = "Invalid credentials."

        else:
            message = "Fields incomplete."
            error = True
    else:
        form = ConnectionForm()
    return render(request, "login/login.html", locals())

