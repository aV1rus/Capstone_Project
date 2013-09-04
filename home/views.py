# Create your views here.
from django.http import *


def home(request):
    text = """<p> This is a sample view in python"""
    return HttpResponse(text)