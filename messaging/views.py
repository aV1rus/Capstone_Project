from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url="login.views.connect")
def messaging(request):
    return render_to_response('home/messaging/messaging.html',locals())

# class MessagingTemp(TemplateView):
#     template_name = 'hello_class.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MessagingTemp, self).get_context_data(**kwargs)
#         context['name'] = 'Nick'
#         return context