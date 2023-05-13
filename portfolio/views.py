from django.shortcuts import render, redirect

from portfolio.models import *
from .forms import *


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


def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "project_form.html", context)


def edit_project(request, pk):
    project = Projects.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "project_form.html", context)


def delete_project(request):
    context = {}
    return render(request, "project_form.html", context)


def inbox(request):
    messages = Messages.objects.all()
    context = {"messages": messages}
    return render(request, "inbox.html", context)


def contact_form(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "contact_form.html", context)
