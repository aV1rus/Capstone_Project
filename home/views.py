# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from sections.messaging.models import PrivateMessage

@login_required(login_url="login.views.connect")
def home(request):
    request.session['messages'] = PrivateMessage.objects.filter(receiver=request.user, viewed=False).count()
    return redirect("sections.newsfeed.views.newsfeed")

    # return render(request, 'home/home.html', locals())
