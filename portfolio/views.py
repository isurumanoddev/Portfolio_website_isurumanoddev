import os

from django.shortcuts import render, redirect

from Portfolio_website_isurumanoddev import settings
from portfolio.models import *
from .forms import *

from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas


class GeneratePDF(View):
    def get(self, request):
        file_name = 'a.pdf'
        file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', file_name)

        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        os.remove(file_path)  # Remove the temporary file.

        return HttpResponse('Error generating PDF file.', status=400)


# Create your views here.
def home(request):
    projects = Projects.objects.all()[:6]
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"projects": projects, "form": form}
    return render(request, "index.html", context)


def projects(request):
    projects = Projects.objects.all()
    context = {"projects": projects}
    return render(request, "projects.html", context)


def project_page(request, pk):
    project = Projects.objects.get(id=pk)
    context = {"project": project}
    return render(request, "project_page.html", context)

def skills(request):
    skills = Skills.objects.all()
    context = {"skills": skills}
    return render(request, "skills.html",context)
def add_skill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "skills_form.html", context)

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
