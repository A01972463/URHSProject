from django.shortcuts import render

from .models import Student, Course

# Create your views here.
def index(request):
    return render(request, 'ApexTracker/index.html')

def input(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'ApexTracker/input.html',
                  {"students": students})

def report(request):
    return render(request, 'ApexTracker/report.html')

def settings(request):
    return render(request, 'ApexTracker/settings.html')
