from django.shortcuts import render
from .models import Project

def home(request):
    models = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'models': models})