from django.shortcuts import render

from .models import Project


# Create your views here.
def index(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'profile.html', {'projects': projects})
