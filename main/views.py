from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()[:3]
    return render(request, 'home.html', {'projects': projects})


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')