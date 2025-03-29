from django.shortcuts import render
from django.http import HttpResponseRedirect
from ProjectA import settings
from django.views.generic import TemplateView


def entrypoint(request):
    if settings.DEBUG:
        return HttpResponseRedirect('http://localhost:5173')
    else:
        return TemplateView.as_view(template_name='index.html')

