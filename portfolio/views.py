from django.shortcuts import render

from portfolio.models import *


# Create your views here.
def home(request):
    projects = Projects.objects.all()
    context = {"projects": projects}
    return render(request, "index.html", context)


def projects(request):
    projects = Projects.objects.all()
    context = {"projects": projects}
    return render(request, "projects.html", context)


def project_page(request, pk):
    project = Projects.objects.get(id=pk)
    context = {"project": project}
    return render(request, "project_page.html", context)
