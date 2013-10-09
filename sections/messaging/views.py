from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import RequestContext
from sections.messaging.forms import Compose
from sections.messaging.models import PrivateMessage

@login_required(login_url="login.views.connect")
def messaging(request):
    return render_to_response('home/messaging/messaging.html', locals())

@login_required(login_url="login.views.connect")
def compose(request):
    notify =False
    message = ""
    if request.method == 'POST':
        form = Compose(request.POST)
        if form.is_valid():
            receiver = form.cleaned_data['receiver']
            content = form.cleaned_data['content']
            PrivateMessage(sender=request.user, receiver=receiver, content=content).save()
            notify = True
            message = "message sent !"
        else:
            notify = True
            message = 'Message is incomplete !'
    else:
        form = Compose()

    return render_to_response('home/messaging/compose.html', locals(), context_instance=RequestContext(request))
# class MessagingTemp(TemplateView):
#     template_name = 'hello_class.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MessagingTemp, self).get_context_data(**kwargs)
#         context['name'] = 'Nick'
#         return context