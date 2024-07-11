from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ApexTracker/index.html')

def input(request):
    return render(request, 'ApexTracker/input.html')

def report(request):
    return render(request, 'ApexTracker/report.html')

def settings(request):
    return render(request, 'ApexTracker/settings.html')
